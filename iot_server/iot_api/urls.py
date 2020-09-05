from django.contrib import admin
from django.urls import path
from .views import Detail_Data,List_Data

urlpatterns = [
    path('<int:pk>/',Detail_Data.as_view(), name = 'API_detail'),
    path('',List_Data.as_view(), name = 'API'),
]