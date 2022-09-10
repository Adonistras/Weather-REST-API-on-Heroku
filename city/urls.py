from django.urls import path, include
from rest_framework import routers
from .views import CityApiViewset, CityCreateView, CityRetrieveView

router = routers.DefaultRouter()
router.register(r'city', CityApiViewset, basename='city')



urlpatterns = [
    path('', include(router.urls)),
    path('create', CityCreateView.as_view(), name='create_city'),
    path('detail/<int:pk>', CityRetrieveView.as_view(), name='get_city')
]