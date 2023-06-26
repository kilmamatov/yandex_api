from django.contrib import admin
from django.urls import path, include
import core.urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('', include(core.urls)),
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
]
