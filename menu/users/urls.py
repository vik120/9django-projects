from django.urls import path
from django.contrib.auth import  views as authentication_views


from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', authentication_views.LoginView.as_view(template_name = "login.html"), name="login"),
    # path('logout/', authentication_views.LogoutView.as_view(template_name="logout.html"), name="logout")
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_page, name="profile")
]
