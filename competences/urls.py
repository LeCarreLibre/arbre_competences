#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Routes de l'application

Ce programme est sous licence GNU GPL
©2017-2018 Nils et Samuel Van Zuijlen
©2019 Samuel Van Zuijlen
"""

from django.conf.urls import url
from competences.views import ListeProfils, AffichageProfil, ListeCompetences,\
                            AffichageCompetence, AddUser, AddCategorie, AddDetail

urlpatterns = [
    url(r'^$', ListeProfils.as_view()),
    url(r'^profils/$', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profil/(?P<pk>\d+)', AffichageProfil.as_view(),
        name="affichage_profil"),
    url(r'^competences/$', ListeCompetences.as_view(), name="competences"),
    url(r'^competence/(?P<pk>\d+)', AffichageCompetence.as_view(),
        name="affichage_competence"),
    url(r'^adduser/$', AddUser, name="add_user"),
    url(r'^addcategorie/$', AddCategorie, name="add_categorie"),
    url(r'^adddetail/$', AddDetail, name="add_detail"),
]
