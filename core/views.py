from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, FormView, TemplateView
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from core import models, forms, filters, logic, serializers
import requests
from dadata import Dadata


class Index(FormView):
    template_name = 'core/index.html'
    form_class = forms.Adress

    def form_valid(self, form):
        dadata = Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET)
        address = form.cleaned_data['local']
        result = dadata.clean("address", address)
        lat = result.get('geo_lat')
        lon = result.get('geo_lon')
        count = form.cleaned_data['count']
        u = logic.Url(lat, lon, count)
        headers = {'X-Yandex-API-Key': settings.X_YANDEX_API_KEY}
        qs_parser = requests.get(u.url, headers=headers).json()
        qs = logic.create_model(qs_parser)
        return render(self.request, 'core/adress.html', {'qs': qs})


class AddressParser(TemplateView):
    template_name = 'core/adress.html'


class HistoryWeather(ListView):
    template_name = 'core/history_weather.html'
    queryset = models.Weather.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # называть переменные своими именами
        context['filter'] = filters.WeatherFilter(self.request.GET, queryset=models.Weather.objects.all())
        context['form'] = forms.Searh_history()
        return context


class WeatherDetail(DetailView):  # исправить (использовать detailview)
    template_name = 'core/weather_detail.html'
    model = models.Weather

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['qs'] = self.get_object()
        return c


class WeatherApi(APIView):
    def post(self, request):
        serializer = serializers.SearchSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            dadata = Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET)
            address = serializer.data.get('local')
            result = dadata.clean("address", address)
            lat = result.get('geo_lat')
            lon = result.get('geo_lon')
            count = serializer.data.get('count')
            u = logic.Url(lat, lon, count)
            headers = {'X-Yandex-API-Key': settings.X_YANDEX_API_KEY}
            qs_parser = requests.get(u.url, headers=headers).json()
            weather_data = logic.create_model(qs_parser)
            return Response(model_to_dict(weather_data), status=200)


class WeatherListApiView(ListAPIView):
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer


class WeatherDetailApiView(APIView):
    def get(self, request):
        queryset = models.Weather.objects.filter(pk=self.request.GET.get('pk')).values()
        return Response(queryset)


# def converter(request):
#     if request.method == 'POST':
#         form = forms.Text(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             name = form.cleaned_data['name']
#             command = f'espeak -vru -w {settings.STATIC_ROOT}/{name}.wav "{text}"'
#             subprocess.call(command, shell=True)
#             audio_file = f'core/audio/{name}.wav'
#             return render(request, 'core/converter.html', {'form': form, 'file_path': audio_file})
#     else:
#         form = forms.Text()
#     return render(request, 'core/converter.html', {'form': form})


# class WeatherApiViewSet(ModelViewSet):
#     queryset = models.SearchWeather
#     serializer_class = serializers.SearchSerializer
#
#     @action(methods=['post'], detail=False)
#     def address(self, request):
#         serializer = serializers.SearchSerializer(data=request.data)
#         if serializer.is_valid():
#             dadata = Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET)
#             address = serializer.data.get('locality')
#             result = dadata.clean("address", address)
#             lat = result.get('geo_lat')
#             lon = result.get('geo_lon')
#             count = serializer.data.get('count')
#             u = logic.Url(lat, lon, count)
#             headers = {'X-Yandex-API-Key': settings.X_YANDEX_API_KEY}
#             qs_parser = requests.get(u.url, headers=headers).json()
#             weather_data = logic.create_model(qs_parser)
#             return Response(weather_data.data, status=200)

# def adress_parser(request):
#     if request.method == 'POST':
#         form = forms.Adress(request.POST)
#         if form.is_valid():
#             lat, lon, count = logic.dadata_func(request, form)
#             u = logic.Url(lat, lon, count)
#             headers = {'X-Yandex-API-Key': settings.X_YANDEX_API_KEY}
#             qs_parser = requests.get(u.url, headers=headers).json()
#             weather_data = logic.create_model(qs_parser)
#             return render(request, 'core/adress.html', {'form': form, 'qs': weather_data})
#     else:
#         form = forms.Adress()
#     return render(request, 'core/adress.html', {'form': form})


