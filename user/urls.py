from django.urls import path, include
from rest_framework import routers
from .views import RetrieveUpdateUserAPI, ListUsers, CreateUserAPI

router = routers.DefaultRouter()
router.register(r'', ListUsers)

urlpatterns = [
    path('retrieve/<int:pk>', RetrieveUpdateUserAPI.as_view(), name='user-retrieved'),
    path('create', CreateUserAPI.as_view(), name='create-user'),
    path('', include(router.urls))
]
