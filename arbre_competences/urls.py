#!/usr/bin/env python
# -*-coding:utf-8 -*

# Ce programme est sous licence GNU GPL
# ©2017 Nils et Samuel Van Zuijlen

"""arbre_competences URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app.views import ListeProfils, AffichageProfil

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profils/$', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profil/(?P<pk>\d+)', AffichageProfil.as_view(), name="affichage_profil")
]
