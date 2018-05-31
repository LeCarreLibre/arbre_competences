#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Routes de l'application

Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.conf.urls import url
from competences.views import ListeProfils, AffichageProfil, ListeCompetences,\
                            AffichageCompetence, add_user

urlpatterns = [
    url(r'^$', ListeProfils.as_view()),
    url(r'^profils/$', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profil/(?P<pk>\d+)', AffichageProfil.as_view(),
        name="affichage_profil"),
    url(r'^competences/$', ListeCompetences.as_view(), name="competences"),
    url(r'^competence/(?P<pk>\d+)', AffichageCompetence.as_view(),
        name="affichage_competence"),
    url(r'^adduser/$', add_user, name="add_user"),
]
