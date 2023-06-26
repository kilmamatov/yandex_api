from django.contrib import admin
from core import models


@admin.register(models.Weather)
class Weather(admin.ModelAdmin):
    list_display = ('local', 'now_dt',)



