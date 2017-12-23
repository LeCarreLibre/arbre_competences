#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Vues de l'application
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from competences.models import Profil, Categorie
from competences.forms import AddUserForm, ConnexionForm


class ListeProfils(ListView):
    """Liste des profils utilisateurs"""

    model = Profil
    context_object_name = "liste_profils"
    template_name = "competences/liste_profils.html"


class AffichageProfil(DetailView):
    """Affichage détaillé du profil d'un utilisateur"""

    model = Profil
    context_object_name = "profil"
    template_name = "competences/affichage_profil.html"


class ListeCompetences(ListView):
    """Liste des categories de competences disponibles"""

    model = Categorie
    context_object_name = "liste_competences"
    template_name = "competences/liste_competences.html"


class AffichageCompetence(DetailView):
    """Affichage détaillé des personnes possédant le compétence"""
    
    model = Categorie
    context_object_name = "competence"
    template_name = "competences/affichage_competence.html"


@login_required
def add_user(request):
    form = AddUserForm(request.POST or None)
    if form.is_valid():
        lastname = form.cleaned_data['lastname']
        firstname = form.cleaned_data['firstname']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        telephone = form.cleaned_data['telephone']
        voluntary = form.cleaned_data['voluntary']
        addresses = form.cleaned_data['addresses']

        envoi = True

    return render(request, 'competences/add_user.html', locals())

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: # Si l'objet renvoyé n'est pas None
                login(request, user) # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'competences/connexion.html', locals())

def deconnexion(request):
    logout(request)

    return HttpResponseRedirect(reverse(connexion))
