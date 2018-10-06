# -*-coding:utf-8 -*-
"""

Vues de l'application
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""


from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib import messages

from utilisateurs.models import Profil
from competences.models import Categorie, Detail
from competences.forms import AddUserForm, AddCategorieForm, AddDetailForm


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


@permission_required(['auth.add_user', 'competences.add_profil'])
def AddUser(request):
    """Ajout d'un utilisateur et de ses coordonnées"""

    form = AddUserForm(request.POST or None)

    if form.is_valid():
        lastname = form.cleaned_data['lastname']
        firstname = form.cleaned_data['firstname']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        telephone = form.cleaned_data['telephone']
        voluntary = form.cleaned_data['voluntary']
        addresses = form.cleaned_data['addresses']

        user = User.objects.create_user(username, email, "0")
        user.first_name, user.last_name = firstname, lastname
        user.set_unusable_password()
        user.save()

        profil = Profil()
        profil.user = user
        profil.telephone, profil.benevole = telephone, voluntary
        profil.adresse = addresses
        profil.save()

        messages.add_message(request, messages.SUCCESS, "Vous venez d'\
enregistrer un nouvel utilisateur!")

        return redirect("liste_profils")
    else:
        return render(request, 'competences/add_user.html', {"form": form})

@permission_required(['competences.add_categorie'])
def AddCategorie(request):
    """Ajout d'une nouvelle catégorie"""

    form = AddCategorieForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        desc = form.cleaned_data['desc']

        categorie = Categorie()
        categorie.nom = name
        categorie.description = desc
        categorie.save()

        messages.add_message(request, messages.SUCCESS, "Vous venez d'\
enregistrer une nouvelle catégorie de compétence!")

        return redirect("liste_profils")
    else:
        return render(request, 'competences/add_categorie.html', {"form": form})

@permission_required(['competences.add_detail'])
def AddDetail(request):
    """Ajout d'un nouveau détail"""

    form = AddDetailForm(request.POST or None)

    if form.is_valid():
        user = form.cleaned_data['user']
        categorie = form.cleaned_data['categorie']
        details = form.cleaned_data['details']

        detail = Detail()
        detail.user = user
        detail.categorie = categorie
        detail.details = details
        detail.save()

        messages.add_message(request, messages.SUCCESS, "Vous venez d'\
enregistrer un nouveau détail!")

        return redirect("liste_profils")
    else:
        return render(request, 'competences/add_detail.html', {"form": form})
