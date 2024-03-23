from django.urls import  path
from . import views

app_name = 'Movies'
urlpatterns = [
    path('', views.MovieListView.as_view(), name='list')
]