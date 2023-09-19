from django.contrib import admin
from django.urls import path, reverse_lazy
from . import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('reg/', userViews.RegisterPage.as_view(), name='register'),
    path('auth/', authViews.LoginView.as_view(template_name='users/auth.html', next_page='/'), name='auth'),
    path('profile/', userViews.profile, name='profile'),
    path('exit/', authViews.LogoutView.as_view(template_name='main/home.html'), name='exit'),
    path('links/', userViews.links, name='links'),
]