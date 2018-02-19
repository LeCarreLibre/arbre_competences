#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
Modèles de la BdD
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    """Informations supplémentaires sur les utilisateurs"""

    user = models.OneToOneField(User)
    # La liaison OneToOne vers le modèle User
    telephone = models.CharField(null=True, verbose_name="N° de téléphone",
                                 max_length=20)
    benevole = models.BooleanField(default=False)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
