from django.shortcuts import render
from rest_framework import viewsets
from .serialziers import MovieSerializer
from .models import MovieData

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(movie_type='action')
    serializer_class = MovieSerializer