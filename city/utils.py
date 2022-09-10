from WeatherAPI.settings import API_URL, API_ICON
from .models import City
from weather.models import Weather

def create_weather(url, city):
    Weather.objects.create(city=City.objects.get(name=city), temp=url['main']['temp'],
                           wind=url['wind']['speed'], pressure=url['main']['pressure'],
                           clouds=url['weather'][0]['description'],
                           icon=API_ICON.format(url['weather'][0]['icon']))

def update_weather(url, kwargs):
    city = City.objects.get(pk=kwargs['pk'])
    Weather.objects.filter(city=city).update(city=city, temp=url['main']['temp'],
                           wind=url['wind']['speed'], pressure=url['main']['pressure'],
                           clouds=url['weather'][0]['description'],
                           icon=API_ICON.format(url['weather'][0]['icon']))