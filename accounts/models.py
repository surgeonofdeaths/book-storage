from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(
        _('email address'),
        help_text=_("Required email"),
        unique=True,
        blank=True,
    )


class Profile(models.Model):
    MALE = 'male'
    FEMALE = 'female'

    GENDERS = [
        (None, 'Not stated'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    gender = models.CharField(choices=GENDERS, max_length=6, blank=True, verbose_name='Пол пользователя')
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.svg', verbose_name='Аватар пользователя')
    bio = models.TextField(blank=True, verbose_name='Информация о пользователе')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['user']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        pass
