from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(
        _('email address'),
        help_text=_("Required email"),
        blank=True,
        null=True,
    )
    slug = models.SlugField(null=True, unique=True, verbose_name='SLUG')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_profile', kwargs={'slug': self.slug})
