from django.db import models
from user.models import UserAPI
from city.models import City
from weather.models import Weather

class WeatherForecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='weather_forecast', verbose_name='City_id')
    user = models.ForeignKey(UserAPI, on_delete=models.PROTECT, related_name='weather_forecast', verbose_name='User_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')

    def __str__(self):
        return f'{self.user}--{self.city}'

    class Meta:
        ordering = ['-created']
        verbose_name = 'weather forecast'
        verbose_name_plural = 'weather forecast'

