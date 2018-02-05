#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Classes de configuration de l'interface d'administration

Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.contrib import admin
from django.utils.text import Truncator
from competences.models import  Categorie, Detail


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

    def details_court(self, detail):
        """
        Retourne les 40 premiers caractères du contenu de l'article, suivi de
        points de suspension si le texte est plus long.
        """
        return Truncator(detail.details).chars(40, truncate='...')

    details_court.short_description = 'Aperçu du contenu'

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Detail, DetailAdmin)
