#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Application's Routes
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.conf.urls import url
from accounts.views import Login, Logout

urlpatterns = [
    url(r'^login/$', Login, name="connexion"),
    url(r'^logout/$', Logout, name="deconnexion"),
]
