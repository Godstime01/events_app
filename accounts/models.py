from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUserModel(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='user')
    bio = models.TextField(blank=True, null=True, default='mysterious user')
    profile_img = models.ImageField(upload_to='profile/', default='default.webp')


