from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('orders:index')

    else:
        form = SignUpForm()
        return render(request, "accounts/signup.html", {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('orders:index')
        else:
            return render(request, "accounts/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return render(request, "accounts/login.html", {"message": "Logged out."})
