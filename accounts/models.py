from django.db import models
from django.contrib.auth.models import AbstractUser
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
        if not self.id:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)
