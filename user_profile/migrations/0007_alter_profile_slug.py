# Generated by Django 4.1.7 on 2023-03-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='SLUG'),
        ),
    ]