from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = models.MovieData
        fields = ['id', 'name', 'duration', 'rating', 'movie_type', 'banner']
