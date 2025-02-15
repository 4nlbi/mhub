# Generated by Django 4.2.13 on 2024-10-25 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, upload_to='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.ImageField(upload_to='movies')),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('actors', models.CharField(max_length=200)),
                ('youtube_trailer_link', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hubapp.category')),
            ],
        ),
    ]
