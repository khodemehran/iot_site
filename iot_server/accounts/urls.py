from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.loginview, name = 'login'),
    
]