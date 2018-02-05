#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

Modèles de la BdD
Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django.db import models

class Categorie(models.Model):
    """Catégories de compétences"""

    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "Compétences en {0}".format(self.nom)


class Detail(models.Model):
    """Détails des compétences par utilisateur"""

    details = models.TextField()
    user = models.ForeignKey('accounts.Profil', verbose_name="utilisateur concerné")
    categorie = models.ForeignKey('Categorie')

    def __str__(self):
        return self.details
