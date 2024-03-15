from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .models import CustomUser


def homeView(request):
    return render(request, "main/index.html")


def aboutView(request):
    return render(request, "main/about.html")


def sign_up_View(request):
    if request.method == "POST":
        user = CustomUser()
        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.set_password(request.POST.get("password"))
        user.email = request.POST.get("email")
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign_up.html", {})


def sign_in_View(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        print("================USER ===============")
        print(user)
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign_in.html", {})


def logout_View(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")