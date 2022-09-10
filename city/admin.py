from django.contrib import admin
from .models import City
from weather.models import Weather

class WeathersAdminTab(admin.TabularInline):
    model = Weather
    fields = ('created', 'temp', 'wind', 'pressure', 'clouds')
    readonly_fields = ('created', 'wind', 'pressure', 'clouds')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created')
    list_filter = ('name', 'created')
    search_fields = ('name', )
    inlines = (WeathersAdminTab, )
