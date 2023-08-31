from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect  # для отправки html по запросу пользователя
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Advertisement
from .forms import AdvertisementForm
# Create your views here.


# представление
def index(request):
    title = request.GET.get("query")
    if title:
        advertisement = Advertisement.objects.filter(title__icontains=title)  # фильтрация по заголовку
    else:
        advertisement = Advertisement.objects.all()  # показывает все объявления пользователю
    context = {"advertisements": advertisement,
               "title": title}
    return render(request, "app_adv/index.html", context)


def advertisements_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {"advertisement": advertisement}
    return render(request, "app_adv/advertisement.html", context)


def top_sellers(request):
    User = get_user_model()
    # count считает кол-во объявлений, order_by("-adv_count") - сортирует по убыванию из-за "-"
    users = User.objects.annotate(adv_count=Count("advertisement")).order_by("-adv_count")
    context = {"users": users}
    return render(request, "app_adv/top-sellers.html", context)


# декоратор перенаправляет на страницу входа в случае, если пользователь не прошел аутентификацию
@login_required(login_url=reverse_lazy("login"))
def adv_post(request):
    if request.method == "POST":  # если пользователь отправил POST-запрос
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)  # ** - распаковывает словарь, * - распаковывает список
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main-page")  # генерация url по имени
            # возвращение на главную страницу при успешном создании товара
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {"form": form}  # передача описанной формы представлению
    return render(request, "app_adv/advertisement-post.html", context)
# price__lt - меньше, чем(строго)
# price__gt - больше, чем(строго)
# price__gte - равно или больше, чем
# price__lte - равно или меньше, чем
# price__contains
