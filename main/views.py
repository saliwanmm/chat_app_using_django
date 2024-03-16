
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib.auth.models import User

# User's views here.
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


def profile_View(request, id):
    custon_user = get_object_or_404(CustomUser, id=id)

    if request.method == "POST":
        custon_user.username = request.POST.get("username")
        custon_user.first_name = request.POST.get("first_name")
        custon_user.last_name = request.POST.get("last_name")
        custon_user.email = request.POST.get("email")
        custon_user.phone_number = request.POST.get("phone_number")

        avatar = request.FILES.get("avatar")
        if avatar:
            # Save the file to the media directory
            file_name = default_storage.save("avatars/" + avatar.name, ContentFile(avatar.read()))
            # Set the avatar field to the file path
            custon_user.avatar = file_name

        password = request.POST.get("password")
        if password:
            hashed_password = make_password(password)
            custon_user.password = hashed_password

        custon_user.save()
        if custon_user:
            login(request, custon_user)
        return redirect("/")
    else:
        custon_user = CustomUser.objects.get(id=id)
        return render(request, "main/profile.html", {
            "custon_user": custon_user,
        })
