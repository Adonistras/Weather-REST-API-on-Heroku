from rest_framework import serializers
from .exceptions import CityDoesNotExists
from .models import City
from weather.serializers import WeatherSerializer
from WeatherAPI.settings import API_FULL_URL
import requests
from .utils import create_weather


class CitySerializer(serializers.ModelSerializer):
    weather = WeatherSerializer(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'created', 'weather')


class CityCreateSerializer(serializers.ModelSerializer):
    weather = WeatherSerializer(many=True, read_only=True)

    def create(self, validated_data):
        city = validated_data.get('name')
        result = requests.get(API_FULL_URL.format(city)).json()
        if result['cod'] == 200:
            instance = City.objects.get_or_create(**validated_data)
            create_weather(result, city)
            return instance[0]
        else:
            raise CityDoesNotExists

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'created', 'weather')


