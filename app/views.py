#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.models import Profil

class ListeProfils(ListView):
    model = Profil
    context_object_name = "liste_profils"
    template_name = "app/liste_profils.html"

class AffichageProfil(DetailView):
    model = Profil
    context_object_name = "profil"
    template_name = "app/affichage_profil.html"
