#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Application's Views
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from accounts.forms import ConnexionForm

def Login(request):
    """ Login view """

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("liste_profils")
    else:
        form = ConnexionForm()

    return render(request, 'accounts/login.html', {"form": form})


def Logout(request):
    """ Logout view """

    logout(request)

    return HttpResponseRedirect('/accounts/login')
