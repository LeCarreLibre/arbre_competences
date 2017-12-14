#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Vues de l'application
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

# from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from competences.models import Profil, Categorie
from competences.forms import AddUser


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


def adduser(request):
    form = addser(request.POST or None)
    if form.is_valid():
        lastname = form.cleaned_data['lastname']
        firstname = form.cleaned_data['firstname']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        telephone = form.cleaned_data['telephone']
        voluntary = form.cleaned_data['voluntary']
        addresses = form.cleaned_data['addresses']

        envoi = True

    return render(request, 'competences/new_user.html', locals())
