# Generated by Django 4.1.7 on 2023-03-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('', 'Not stated'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, verbose_name='Пол пользователя'),
        ),
    ]
