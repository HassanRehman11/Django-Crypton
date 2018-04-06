
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from coin import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
