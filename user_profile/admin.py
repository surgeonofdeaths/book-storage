from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender']
    prepopulated_fields = {'slug': ('user', )}
    list_display_links = ['user']