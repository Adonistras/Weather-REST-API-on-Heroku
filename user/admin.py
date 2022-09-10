from django.contrib import admin
from .models import UserAPI

@admin.register(UserAPI)
class UserAPIAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'email')
    list_filter = ('username', 'gender')
    search_fields = ('username', )
