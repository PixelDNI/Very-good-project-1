# Generated by Django 4.2.3 on 2023-07-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_bookrent_book_remove_bookrent_reader_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_surname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reader',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
