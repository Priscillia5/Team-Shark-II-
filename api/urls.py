from . import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('home/', views.HelloView.as_view()),
    path('auth/register', views.UserCreate.as_view()),
    path('auth/login', obtain_auth_token, name='api_token_auth')
]