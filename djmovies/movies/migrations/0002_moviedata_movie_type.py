# Generated by Django 5.0.1 on 2024-03-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='movie_type',
            field=models.CharField(default='action', max_length=20),
        ),
    ]
