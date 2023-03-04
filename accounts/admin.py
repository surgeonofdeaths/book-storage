from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'email', 'is_staff')
    ordering = ('is_staff', 'username', 'email')
    search_fields = ('username', 'email')
    list_display_links = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender']
