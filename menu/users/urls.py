from django.urls import path

from . import views

app_name='register'
url_pattern = [
    path('', views.register, name="register")
]