# -*-coding:utf-8 -*-
"""
Application's Forms

Ce programme est sous licence GNU GPL
©2017 Nils et Samuel Van Zuijlen
"""
from django import forms


class AddUserForm(forms.Form):
    """create an user in a simple way"""

    lastname = forms.CharField(max_length=100, label="Nom")
    firstname = forms.CharField(max_length=100, label="Prénom")
    username = forms.CharField(max_length=100, label="Nom d'utilisateur")
    email = forms.EmailField(label="Adresse mail du nouvel utilisateur")
    telephone = forms.CharField(min_length=10, max_length=15)
    voluntary = forms.BooleanField(help_text="Cochez si La personne souhaite "
                                             "être bénévole.", label="Bénevole", required=False)
    addresses = forms.CharField(label="Adresse")
