from django.urls import path
from rest_framework.routers import DefaultRouter
import core.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', core.views.Index.as_view()),
    path('adress_parser/', core.views.AddressParser.as_view()),
    path('history_weather/', core.views.HistoryWeather.as_view()),
    path('weather_delail/<int:pk>', core.views.WeatherDetail.as_view()),
    path('api/v1/weather_list/', core.views.WeatherListApiView.as_view()),
    path('api/v1/', core.views.WeatherApi.as_view()),
    path('api/v1/detail/', core.views.WeatherDetailApiView.as_view()),
    # path('api/address', core.views.Weather.as_view()),
    # path('converter/', core.views.converter),
]


urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
router = DefaultRouter()
# router.register('api/v1', core.views.WeatherApiViewSet, basename='address')
urlpatterns += router.urls
