from django.contrib import admin
from .models import Weather
from django.utils.html import mark_safe

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'temp', 'get_icon')
    list_filter = ('city', 'created')
    search_fields = ('city', 'created')
    fields = ('city', 'created', 'temp', 'wind', 'pressure', 'clouds')
    readonly_fields = ('city', 'created', 'wind', 'pressure', 'clouds')

    def get_icon(self, obj):
        return mark_safe(f'<img src="{obj.icon}" width="50", height=60">')

