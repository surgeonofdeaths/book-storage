from django.conf import settings
from django.db import models

from django.urls import reverse

MALE = 'male'
FEMALE = 'female'

GENDERS = [
    (None, 'Not stated'),
    (MALE, 'Male'),
    (FEMALE, 'Female'),
]


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='Пользователь')
    slug = models.SlugField(unique=True, verbose_name='SLUG')
    gender = models.CharField(choices=GENDERS, max_length=6, blank=True, verbose_name='Пол пользователя')
    avatar = models.ImageField(blank=True, upload_to='avatars/', verbose_name='Аватар пользователя')
    bio = models.TextField(blank=True, verbose_name='Информация о пользователе')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'
        ordering = ['user']

    def __str__(self):
        return self.user.username[:30]

    def get_absolute_url(self):
        return reverse('view_profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.user.slug
        super().save(*args, **kwargs)