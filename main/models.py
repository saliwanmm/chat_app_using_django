from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add your custom fields here
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)