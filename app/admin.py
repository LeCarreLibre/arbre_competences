#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Ce programme est sous licence GNU GPL
# ©2017 Nils et Samuel Van Zuijlen

from django.contrib import admin
from django.utils.text import Truncator

from app.models import Profil, Categorie, Detail

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'adresse', 'benevole')
    list_filter = ('benevole',)
    #date_hierarchy = 'user.date_joined'
    #ordering = ('user.date_joined', )
    search_fields = ('telephone',) # 'user.first_name', 'user.last_name', 

admin.site.register(Profil, ProfilAdmin)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    ordering = ('nom',)
    search_fields = ('nom', 'description')

admin.site.register(Categorie, CategorieAdmin)

class DetailAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'user', 'details_court')
    list_filter = ('categorie', 'user')
    ordering = ('categorie',)
    search_fields = ('details',)
    fields = ('user', 'categorie', 'details')

    def details_court(self, detail):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(detail.details).chars(40, truncate='...')

    details_court.short_description = 'Aperçu du contenu'
#
admin.site.register(Detail, DetailAdmin)
