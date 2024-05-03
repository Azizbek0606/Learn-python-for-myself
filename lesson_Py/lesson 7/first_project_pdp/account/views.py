from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.db import IntegrityError


def login_view(request):
    return render(request, "register/login.html")


def login_method(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Wrong username or password")
            return redirect("/login/user/login")
    else:
        return redirect("/login/user/login")

def signup_method(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            messages.error(request, "Passwords must match.")
            return redirect("/login/user/login")

        try:
            user = User.objects.create_user(username, email, password)
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")
        except IntegrityError:
            messages.error(request, "Username or email already exists.")
            return redirect("/login/user/login")
        except Exception as e:
            messages.error(request, str(e))
            return redirect("/login/user/login")
    else:
        return redirect("/login/user/login")


def logout_method(request):
    logout(request)
    return redirect("/login/user/login")

def profile_view(request):
    return render(request, "user/user_panel.html")
