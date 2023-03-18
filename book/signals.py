from django.core.files import File
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

from pdf2image import convert_from_path
import os

from .models import Book


@receiver(post_save, sender=Book)
def first_page_to_cover(sender, instance, created, **kwargs):
    if created:
        path_to_poppler = r'C:\Program Files\poppler-23.01.0\Library\bin'
        upload_to = settings.BASE_DIR / 'uploads' / 'covers'
        cover = convert_from_path(
            pdf_path=instance.pdf.path,
            output_folder=upload_to,
            poppler_path=path_to_poppler,
            last_page=1,
            fmt='jpg',
        )[0]
        absolute_path = cover.filename
        with open(absolute_path, 'rb') as image:
            instance.cover.save(
               os.path.basename(absolute_path),
               File(image),
            )
