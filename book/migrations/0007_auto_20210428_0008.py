# Generated by Django 3.1.6 on 2021-04-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_copies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copies',
        ),
        migrations.AddField(
            model_name='book',
            name='NumberOfCopies',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
