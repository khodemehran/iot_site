from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('data.urls')),
    path('api/', include('iot_api.urls')),
    path('weather/', include('weather_app.urls')),
    path('api-auth/', include('rest_framework.urls')), # new 
    path('accounts/',include('accounts.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),# new 
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    
]
