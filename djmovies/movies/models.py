from django.db import models

# Create your models here.

class MovieData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.FloatField()
    duration = models.FloatField()
    movie_type = models.CharField(max_length=20, default='action')
    banner = models.ImageField(upload_to='static/image', default='')

    def __str__(self):
        return self.name
