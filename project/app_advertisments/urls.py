# маршрутизатор приложения
from django.urls import path
from .views import index, test, top_sellers


urlpatterns = [path("", index),
               path("test/", test),
               path("top_sellers/", top_sellers)]
