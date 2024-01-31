from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.details, name='details'),
    path('add/', views.create_item, name='add')
]
