from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'email', 'is_staff')
    ordering = ('is_staff', 'username', 'email')
    search_fields = ('username', 'email')
    list_display_links = ('username', 'email')
    prepopulated_fields = {'slug': ('username',)}

    fieldsets = (
        (None, {"fields": ("username", "slug", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        None,
        {
            'classes': ('wide',),
            'fields': ('username', 'slug', 'email', 'password1', 'password2'),
        },
    )
