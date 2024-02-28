from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    # path('<int:item_id>/', views.details, name='details'),
    path('<int:pk>/', views.FoodDetails.as_view(), name='details'),
    path('add/', views.CreateItem.as_view(), name='add'),
    path('update/<int:item_id>/', views.update_item, name='update'),
    path('delete/<int:item_id>/', views.delete_item, name='delete')
]
