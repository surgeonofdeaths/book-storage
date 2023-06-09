# Generated by Django 4.1.7 on 2023-03-04 21:07

import book.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автора',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='SLUG')),
                ('content', models.TextField(null=True, verbose_name='Описание')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Обложка')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='books/', verbose_name='PDF')),
                ('total_pages', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество страниц')),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German'), ('ru', 'Russian'), ('ua', 'Ukrainian'), ('pl', 'Polish')], max_length=25, verbose_name='Язык')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('isbn', models.CharField(blank=True, max_length=30, validators=[book.validators.validate_isbn], verbose_name='ISBN')),
                ('author', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='books', to='book.author', verbose_name='Автор книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-published_date', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='CommentBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Коммент')),
                ('date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='book.book', verbose_name='Книга')),
                ('user', models.ForeignKey(default='Deleted', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='select_books', to='book.topic', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='select_books', to=settings.AUTH_USER_MODEL, verbose_name='Опубликовал'),
        ),
    ]
