from django.db import models
from city.models import City


class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City', related_name='weather', null=True)
    temp = models.CharField(max_length=5, verbose_name='Temperature in C', )
    wind = models.CharField(max_length=50, verbose_name='Wind')
    pressure = models.CharField(max_length=50, verbose_name='Pressure')
    clouds = models.CharField(max_length=50, verbose_name='Clouds')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    icon = models.CharField(max_length=200, verbose_name='Icon')

    def __str__(self):
        return f'Temperature at {self.city} at {self.created}'

    class Meta:
        ordering = ['-created']
        verbose_name = 'Weather'
        verbose_name_plural = 'Weather'


