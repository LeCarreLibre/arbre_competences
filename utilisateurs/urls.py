#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Application's Routes

Ce programme est sous licence GNU GPL
©2017-2018 Nils et Samuel Van Zuijlen
"""

from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView, {'template_name': 'utilisateurs/login.\
html'}, name="connexion"),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': '/'},
        name="deconnexion")
]
