# Generated by Django 4.1.7 on 2023-03-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_content_alter_book_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='total_pages',
            field=models.PositiveIntegerField(verbose_name='Количество страниц'),
        ),
    ]
