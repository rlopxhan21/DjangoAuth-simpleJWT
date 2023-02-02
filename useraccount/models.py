from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    profileImage = ResizedImageField(
        blank=True, null=True, upload_to="users/", default="users/pp.jpg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
