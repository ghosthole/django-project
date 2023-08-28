from django.http import HttpResponse
from django.shortcuts import render, redirect  # для отправки html по запросу пользователя
from django.urls import reverse

from .models import Advertisement
from .forms import AdvertisementForm
# Create your views here.


# представление
def index(request):
    advertisement = Advertisement.objects.all()
    context = {"advertisements": advertisement}
    return render(request, "index.html", context)


def test(request):
    return render(request, "test.html")


def test2(request):
    return render(request, "test2.html")


def top_sellers(request):
    return render(request, "top-sellers.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def profile(request):
    return render(request, "profile.html")


def adv_post(request):
    if request.method == "POST":  # если пользователь отправил POST-запрос
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)  # ** - распаковывает словарь, * - распаковывает список
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main-page")  # возвращение на главную страницу при успешном создании товара
            return redirect(url)  # генерация url по имени
    else:
        form = AdvertisementForm()
    context = {"form": form}  # передача описанной формы представлению
    return render(request, "advertisement-post.html", context)
