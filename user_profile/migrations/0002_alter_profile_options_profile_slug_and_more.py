# Generated by Django 4.1.7 on 2023-03-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user'], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профиля'},
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='SLUG'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='avatars/', verbose_name='Аватар пользователя'),
        ),
    ]
