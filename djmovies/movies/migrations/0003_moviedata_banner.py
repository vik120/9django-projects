# Generated by Django 5.0.1 on 2024-03-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_movie_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='banner',
            field=models.ImageField(default='', upload_to='static/image'),
        ),
    ]
