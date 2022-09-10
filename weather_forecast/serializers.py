from rest_framework import serializers

from .exceptions import UserEmailNotFound
from .models import WeatherForecast
from user.serializers import UserSerializer
from city.serializers import CitySerializer
from user.models import UserAPI


class WeatherForecastSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    city = CitySerializer()

    class Meta:
        model = WeatherForecast
        fields = '__all__'

class WeatherForecastCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        user = UserAPI.objects.get(username=validated_data.get('user'))
        if user.email:
            instance = WeatherForecast.objects.create(**validated_data)
            return instance
        else:
            raise UserEmailNotFound

    def to_representation(self, instance):
        representation = super(WeatherForecastCreateSerializer, self).to_representation(instance)
        representation['name'] = instance.city.name
        return representation

    class Meta:
        model = WeatherForecast
        fields = ('user', 'city')



