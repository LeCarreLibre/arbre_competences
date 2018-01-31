#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Classes de configuration de l'interface d'administration

Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.contrib import admin
from django.utils.text import Truncator
from competences.models import Profil, Categorie, Detail


class ProfilAdmin(admin.ModelAdmin):
    """Classe d'administration du modèle Profil"""
    list_display = ('user', 'telephone', 'adresse', 'benevole')
    list_filter = ('benevole',)
    search_fields = ('telephone',)


class CategorieAdmin(admin.ModelAdmin):
    """Classe d'administration du modèle des catégories de compétences"""
    list_display = ('nom', 'description')
    ordering = ('nom',)
    search_fields = ('nom', 'description')


class DetailAdmin(admin.ModelAdmin):
    """Classe d'administration du modèle des détails de compétences"""
    list_display = ('categorie', 'user', 'details_court')
    list_filter = ('categorie', 'user')
    ordering = ('categorie',)
    search_fields = ('details',)
    fields = ('user', 'categorie', 'details')

    @staticmethod
    def details_court(detail):
        """
        Retourne les 40 premiers caractères du contenu de l'article, suivi de
        points de suspension si le texte est plus long.
        """
        return Truncator(detail.details).chars(40, truncate='...')

    details_court.short_description = 'Aperçu du contenu'

admin.site.register(Profil, ProfilAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Detail, DetailAdmin)
