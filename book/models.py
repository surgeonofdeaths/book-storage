from django.db import models
from django.contrib.auth import get_user_model

from .validators import validate_isbn


class Genre(models.Model):
    genre_name = models.CharField(max_length=75)

    def __str__(self):
        return self.genre_name


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    USA = 'en'
    GERMANY = 'de'
    RUSSIA = 'ru'
    UKRAINE = 'ua'
    POLAND = 'pl'

    LANGUAGE_CHOICES = [
        (USA, 'English'),
        (GERMANY, 'German'),
        (RUSSIA, 'Russian'),
        (UKRAINE, 'Ukrainian'),
        (POLAND, 'Polish'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    cover = models.ImageField(upload_to='uploads/covers/%Y/%m', blank=True, null=True)
    pdf = models.FileField(upload_to='uploads/books/%Y/%m', blank=True, null=True)
    total_pages = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество страниц')
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=30, default=USA, verbose_name='Язык')
    published_data = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    isbn = models.CharField(max_length=30, validators=[validate_isbn], verbose_name='ISBN')
    user = models.ForeignKey(
        get_user_model(), null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Опубликовал'
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Автор книги')
    genre = models.ManyToManyField(Genre, related_name='select_books')

    class Meta:
        ordering = ['author', 'title']

    def __str__(self):
        return f'{self.author}: {self.title[:75]}'
