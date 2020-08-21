from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('data.urls')),
    path('api/', include('iot_api.urls')),
    
]
