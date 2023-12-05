from django.contrib import admin

# Register your models here.
from .models import UserProfile, CustomUserModel


admin.site.register(UserProfile)
admin.site.register(CustomUserModel)