from django.contrib import admin
from django.urls import path
from main.views import index, result
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('result/', result, name = 'result')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
