from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """ A serializer for registration of new users """
    password2 = serializers.CharField(
        write_only=True, style={'input_type': 'password'}, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': "password",
                }
            }
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': "Password doesn't match."})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({
                'error': "Email already exists!"
            })

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({
                'error': 'Username already exists!'
            })

        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        user.set_password(password)
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ A serializer for encoding user information in  refresh token."""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['email'] = user.email

        return token


class ProfileDataSerializer(serializers.ModelSerializer):
    """ A serializer for getting profile inforamtion. """
    class Meta:
        model = User
        exclude = ['password']


class BasicInfoChangeSerializer(serializers.ModelSerializer):
    """ A serializer for updating user basic information (username, first_name, last_name, email). """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PasswordChangeSerializer(serializers.ModelSerializer):
    """ A serializer for updating user password. """
    newpassword = serializers.CharField(
        write_only=True, style={'input_type': 'password'}, required=True)
    newpassword2 = serializers.CharField(
        write_only=True, style={'input_type': 'password'}, required=True)

    class Meta:
        model = User
        fields = ['password', 'newpassword', 'newpassword2']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def validate(self, data):
        if not self.context['request'].user.check_password(data.get('password')):
            raise serializers.ValidationError({
                'error': "Wrong old password!"
            })

        if data.get('newpassword') != data.get('newpassword2'):
            raise serializers.ValidationError({
                'error': "New passwords don't match!"
            })

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['newpassword'])
        instance.save()

        return instance


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profileImage']
