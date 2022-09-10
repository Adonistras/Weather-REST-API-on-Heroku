from django.contrib import admin
from django.urls import path, include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/users/', include('user.urls')),
    path('api/v1/cities/', include('city.urls')),
    path('api/v1/forecast/', include('weather_forecast.urls')),

]
