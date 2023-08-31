# маршрутизатор приложения
from django.urls import path
from .views import index, top_sellers, adv_post, advertisements_detail
# login, register, profile


urlpatterns = [path("", index, name="main-page"),
               path("top_sellers/", top_sellers, name="top-sellers"),
               path("adv_post/", adv_post, name="adv-post"),
               path("advertisement/<int:pk>", advertisements_detail, name="adv-detail")]
