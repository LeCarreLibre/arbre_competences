#!/usr/bin/env python
# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Profil, Categorie , Detail

class ListeProfils(ListView):
    model = Profil
    context_object_name = "liste_profils"
    template_name = "app/liste_profils.html"

class AffichageProfil(DetailView):
    model = Profil
    context_object_name = "profil"
    template_name = "app/affichage_profil.html"

class ListeCategories(ListView):
    model = Categorie
    context_object_name = "liste_categories"
    template_name = "app/liste_categories.html"

class AffichageDetails(ListView):
    model = Profil
    context_object_name = "details"
    template_name = "app/affichage_details.html"
