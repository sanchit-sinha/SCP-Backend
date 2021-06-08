from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView ,  name="auth-login")
]