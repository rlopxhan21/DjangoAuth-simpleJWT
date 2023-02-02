from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    profileImage = models.ImageField(
        blank=True, null=True, upload_to="users/", default="users/pp.jpg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
