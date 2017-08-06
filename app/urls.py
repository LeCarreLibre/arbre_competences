#!/usr/bin/env python
# -*-coding:utf-8 -*
from django.conf.urls import url
from app.views import *

urlpatterns = [
	url(r'^', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profils/$', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profil/(?P<pk>\d+)', AffichageProfil.as_view(), name="affichage_profil")
]
