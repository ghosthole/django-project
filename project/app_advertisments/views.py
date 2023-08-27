from django.http import HttpResponse
from django.shortcuts import render  # для отправки html по запросу пользователя
from .models import Advertisement
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
