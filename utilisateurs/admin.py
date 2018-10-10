# -*-coding:utf-8 -*-

"""
Classes de configuration de l'interface d'administration

Ce programme est sous licence GNU GPL
©2017-2018 Nils et Samuel Van Zuijlen
"""

from django.contrib import admin
from utilisateurs.models import Profil


class ProfilAdmin(admin.ModelAdmin):
    """Classe d'administration du modèle Profil"""
    list_display = ('user', 'telephone', 'adresse', 'benevole')
    list_filter = ('benevole',)
    search_fields = ('telephone',)


admin.site.register(Profil, ProfilAdmin)
