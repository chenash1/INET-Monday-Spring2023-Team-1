from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile, DogProfile, EventPost

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(DogProfile)
admin.site.register(EventPost)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
