from dadata import Dadata
from core import models
from django.conf import settings


class Url:
    def __init__(self, lat, lon, count):
        self.url = f"https://api.weather.yandex.ru/v2/forecast?" \
              f"lat={lat}" \
              f"&lon={lon}" \
              f"&lang=ru_RU" \
              f"&limit={count}" \
              f"&hours=False&extra=False"


def create_model(qs_parser):
    if 'locality' in qs_parser['geo_object']:
        locality = qs_parser['geo_object']['locality']['name']
    else:
        locality = 'unknown'
    weather_data = models.Weather.objects.create(
        local=locality,
        data=qs_parser,
    )
    return weather_data


def dadata_func(request, form):
    dadata = Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET)
    address = request.POST.get('local')
    result = dadata.clean("address", address)
    lat = result.get('geo_lat')
    lon = result.get('geo_lon')
    count = form.cleaned_data['count']
    return lat, lon, count



