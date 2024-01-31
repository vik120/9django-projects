from django.db import models


# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_desc = models.TextField(max_length=255)
    item_image = models.CharField(max_length=600, default='https://source.unsplash.com/random/?placeholder')

    def __str__(self):
        return self.item_name
