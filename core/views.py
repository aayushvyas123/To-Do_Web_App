from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *


def home(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            request.session.set_expiry(86400)
            login(request, user)
            return redirect("/")
        else:
            return redirect("home")
    else:
        return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('user created')
        return redirect("home")
    else:
        return render(request, "register.html")


def todoPage(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        todos = todo.objects.filter(user=request.user)
        return render(request, 'todo_page.html', {'todo': todos})
    else:
        return render(request, 'index.html')


def addItem(request):
    if request.user.is_authenticated:
        task_value = request.GET.get("item")
        todos = todo.objects.create(user=request.user, task=task_value)

        return render(request, 'blank.html', {'task_value': task_value})


def deleteItem(request):
    if request.user.is_authenticated:
        task_value = request.GET.get("item")
        todo.objects.filter(user=request.user, task=task_value).delete()
        return render(request, 'blank.html', {'task_value': task_value})


def logout_view(request):
    logout(request)
    return redirect('home')
