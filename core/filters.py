import django_filters
from core import models


class WeatherFilter(django_filters.FilterSet):
    local = django_filters.CharFilter(lookup_expr='iexact')
    now_dt = django_filters.DateTimeFilter()

    class Meta:
        model = models.Weather
        fields = ['local', 'now_dt']



