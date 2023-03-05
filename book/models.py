from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify

from .validators import validate_isbn, validate_topic

User = get_user_model()


class Topic(models.Model):
    name = models.CharField(max_length=75, validators=[validate_topic], verbose_name='Топик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автора'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Book(models.Model):
    USA = 'en'
    GERMANY = 'de'
    RUSSIA = 'ru'
    UKRAINE = 'ua'
    POLAND = 'pl'

    LANGUAGE_CHOICES = [
        (None, 'Choose a language:'),
        (USA, 'English'),
        (GERMANY, 'German'),
        (RUSSIA, 'Russian'),
        (UKRAINE, 'Ukrainian'),
        (POLAND, 'Polish'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(null=True, unique=True, verbose_name='SLUG')
    content = models.TextField(null=True, verbose_name='Описание')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='Обложка')
    pdf = models.FileField(upload_to='books/', blank=True, null=True, verbose_name='PDF')
    total_pages = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество страниц')
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=25, verbose_name='Язык')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    isbn = models.CharField(blank=True, max_length=30, validators=[validate_isbn], verbose_name='ISBN')
    user = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='select_books', verbose_name='Опубликовал'
    )
    author = models.ForeignKey(
        Author, default='unknown', on_delete=models.SET_DEFAULT, related_name='books', verbose_name='Автор книги'
    )
    topics = models.ManyToManyField(Topic, related_name='select_books', verbose_name='Топики')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-published_date', 'author']

    def __str__(self):
        return f'{self.author}: {self.title[:75]}'

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class CommentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name='Книга')
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Deleted', verbose_name='Автор')
    text = models.TextField(verbose_name='Коммент')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:75]
