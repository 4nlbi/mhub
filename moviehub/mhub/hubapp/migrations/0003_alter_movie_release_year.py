# Generated by Django 4.2.13 on 2024-10-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubapp', '0002_alter_movie_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]
