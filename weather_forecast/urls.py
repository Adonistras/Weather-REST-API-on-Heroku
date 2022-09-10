from django.urls import path, include
from rest_framework import routers
from .views import ForecastViewset, ForecastDestroy, ForecastCreate

router = routers.DefaultRouter()
router.register(r'weather', ForecastViewset, basename='weather')



urlpatterns = [
    path('', include(router.urls)),
    path('add', ForecastCreate.as_view(), name='add_forecast'),
    path('delete/<int:pk>', ForecastDestroy.as_view(), name='delete_forecast'),
]