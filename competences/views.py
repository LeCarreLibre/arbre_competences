#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Vues de l'application
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from competences.models import Profil, Categorie


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
