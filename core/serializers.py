from rest_framework import serializers
from core import models


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Weather
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SearchWeather
        fields = '__all__'
