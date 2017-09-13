#!/usr/bin/env python
# -*-coding:utf-8 -*
from django.conf.urls import url
from competences.views import *

urlpatterns = [
	url(r'^categories/?$', ListeCategories.as_view(), name="liste_categories"),
    url(r'^profils/?$', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profil/(?P<pk>\d+)', AffichageProfil.as_view(), name="affichage_profil")
]
