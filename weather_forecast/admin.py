from django.contrib import admin
from .models import WeatherForecast

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'created')
    search_fields = ('user', 'city',)
    list_filter = ('user', 'city', 'created')

