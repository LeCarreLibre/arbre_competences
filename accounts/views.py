from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from accounts.forms import ConnexionForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def Login(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
    else:
        form = ConnexionForm()

    return render(request, 'accounts/login.html', {"form": form})


def Logout(request):
    logout(request)

    return HttpResponseRedirect('/accounts/login')
