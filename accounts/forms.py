# -*-coding:utf-8 -*-
"""
Application's Forms

Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""

from django import forms


class ConnexionForm(forms.Form):
    """ Login form """

    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

