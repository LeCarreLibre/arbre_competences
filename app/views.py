#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""Vues de l'application"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.models import Profil


class ListeProfils(ListView):
	"""Liste des profils utilisateurs"""
    model = Profil
    context_object_name = "liste_profils"
    template_name = "app/liste_profils.html"


class AffichageProfil(DetailView):
	"""Affichage détaillé du profil d'un utilisateur"""
    model = Profil
    context_object_name = "profil"
    template_name = "app/affichage_profil.html"
