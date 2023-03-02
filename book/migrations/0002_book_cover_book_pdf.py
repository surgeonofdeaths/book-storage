# Generated by Django 4.1.7 on 2023-03-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/covers/%Y/%m'),
        ),
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/books/%Y/%m'),
        ),
    ]
