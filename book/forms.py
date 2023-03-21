from django import forms
from django.forms import ModelForm

from .models import Book


# class BookEditForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = (
#             'title', 'content', 'cover', 'total_pages', 'pdf', 'language', 'isbn', 'user', 'topics',
#         )
