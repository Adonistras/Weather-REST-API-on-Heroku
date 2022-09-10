from rest_framework import viewsets, generics
from .models import WeatherForecast
from .serializers import WeatherForecastSerializer, WeatherForecastCreateSerializer
from rest_framework.permissions import IsAuthenticated



class ForecastViewset(viewsets.GenericViewSet):
    serializer_class = WeatherForecastSerializer
    permission_classes = (IsAuthenticated, )
    queryset = WeatherForecast.objects.all()


class ForecastCreate(generics.CreateAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastCreateSerializer
    permission_classes = (IsAuthenticated, )


class ForecastDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastCreateSerializer
    permission_classes = (IsAuthenticated, )