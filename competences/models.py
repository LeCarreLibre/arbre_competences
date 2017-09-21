#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""Modèles de la BdD"""

from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    """Informations supplémentaires sur les utilisateurs"""
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    telephone = models.CharField(null=True, verbose_name="N° de téléphone",
        max_length=20)
    benevole = models.BooleanField(default=False)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)

class Categorie(models.Model):
    """Catégories de compétences"""
    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "Compétences en {0}".format(self.nom)

class Detail(models.Model):
    """Détails des compétences par utilisateur"""
    details = models.TextField()
    user = models.ForeignKey('Profil', verbose_name="utilisateur concerné")
    categorie = models.ForeignKey('Categorie')

    def __str__(self):
        return self.details
