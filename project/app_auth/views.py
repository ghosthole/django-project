from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm


# reverse возвращает ссылку по имени, а reverse_lazy - генератор
# указываем путь, куда нужно направить пользователя в случае, если пользователь не прошел аутентификацию
@login_required(login_url=reverse_lazy("login"))
def profile_view(request):
    return render(request, "app_auth/profile.html")


def login_view(request):
    redirect_url = reverse("profile")
    if request.method == "GET":
        if request.user.is_authenticated:  # если пользователь аутентифицирован
            return redirect(redirect_url)
        else:
            return render(request, "app_auth/login.html")
    # ветка POST-запроса
    username = request.POST.get("username")
    password = request.POST.get("password")
    # параметры должны быть именованными
    user = authenticate(request, username=username, password=password)  # функция аутентифицирует пользователя
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    print(request.user.is_authenticated)
    return render(request, template_name="templates/app_auth/login.html", context={
        "error": "Пользователь не найден."})


def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


def register_view(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST["password1"])
            login(request, user=user)
            return redirect(reverse("profile"))
    else:
        form = ExtendedUserCreationForm()

    context = {
        "form": form
    }
    return render(request, "app_auth/register.html", context)

