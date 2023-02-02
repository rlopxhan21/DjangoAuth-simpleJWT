from rest_framework import generics, mixins, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import RegistrationSerializer, MyTokenObtainPairSerializer, ProfileDataSerializer, BasicInfoChangeSerializer, PasswordChangeSerializer, ProfileImageSerializer
from .permissions import SuperUserorOwnerorReadOnly


class RegisterationView(mixins.CreateModelMixin, generics.GenericAPIView):
    """ A class for registering user """
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serailizer = self.serializer_class(data=request.data)

        if serailizer.is_valid():
            user = serailizer.save()

            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    """ A class for custom token generation and used for login requests. """
    serializer_class = MyTokenObtainPairSerializer


class ProfileDataView(mixins.ListModelMixin, generics.GenericAPIView):
    """ A class for retrieving all user profile data """
    serializer_class = ProfileDataSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SingleProfileDataView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """ A class for retrieving a single user profile data """
    serializer_class = ProfileDataSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class BasicInfoChangeView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """ A class for updating user profile data """
    serializer_class = BasicInfoChangeSerializer
    queryset = User.objects.all()
    permission_classes = [SuperUserorOwnerorReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PasswordChangeView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """ A class for updating user password """
    serializer_class = PasswordChangeSerializer
    queryset = User.objects.all()

    permission_classes = [SuperUserorOwnerorReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProfileImageView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """ A class for updating user profile image """
    serializer_class = ProfileImageSerializer
    queryset = User.objects.all()
    permission_classes = [SuperUserorOwnerorReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
