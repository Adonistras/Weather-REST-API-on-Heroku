from WeatherAPI.settings import API_FULL_URL
from WeatherAPI.celery import app
import requests
from .utils import update_weather
from .models import City


@app.task(name='Update_weather')
def update_every_hour_weather():
    cities = City.objects.all()
    if not cities:
        return
    for city in cities:
        url = API_FULL_URL.format(city.name)
        result = requests.get(url).json()
        update_weather(result, {'pk': city.pk})
    return 'Updated'
