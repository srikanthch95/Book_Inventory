# Generated by Django 2.2.4 on 2021-06-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbooks',
            name='total_borrowed_books',
            field=models.IntegerField(default=False),
        ),
    ]
