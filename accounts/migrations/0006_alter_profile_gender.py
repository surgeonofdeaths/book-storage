# Generated by Django 4.1.7 on 2023-03-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'Not stated'), ('male', 'Male'), ('female', 'Female')], max_length=6, verbose_name='Пол пользователя'),
        ),
    ]
