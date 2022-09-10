import requests
from WeatherAPI.settings import API_FULL_URL
from rest_framework import viewsets, permissions, generics, serializers, status
from .models import City
from .serializers import CitySerializer, CityCreateSerializer
from django.http import QueryDict
from rest_framework.response import Response
from .utils import update_weather



class CityApiViewset(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticated, )



class CityCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
            request.data['name'] = request.data['name'].title()
            request.data._mutable = False
        else:
            request.data['name'] = request.data['name'].title()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CityRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        city = City.objects.get(pk=kwargs['pk']).name
        result = requests.get(API_FULL_URL.format(city)).json()
        update_weather(result, kwargs)
        return self.retrieve(request, *args, **kwargs)


