# маршрутизатор приложения
from django.urls import path
from .views import index, test, top_sellers, adv_post, login, register, profile


urlpatterns = [path("", index, name="main-page"),
               path("test/", test),
               path("top_sellers/", top_sellers, name="top-sellers"),
               path("adv_post/", adv_post, name="adv-post"),
               path("login/", login, name="login"),
               path("register/", register, name="register"),
               path("profile/", profile, name="profile")]
