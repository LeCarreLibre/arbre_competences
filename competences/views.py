#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Ce programme est sous licence GNU GPL
# ©2017 Nils et Samuel Van Zuijlen

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from competences.models import *

class ListeProfils(ListView):
    model = Profil
    context_object_name = "liste_profils"
    template_name = "competences/liste_profils.html"

class AffichageProfil(DetailView):
    model = Profil
    context_object_name = "profil"
    template_name = "competences/affichage_profil.html"

class ListeCategories(ListView):
    model = Categorie
    context_object_name = "liste_categories"
    template_name = "competences/liste_categories.html"
