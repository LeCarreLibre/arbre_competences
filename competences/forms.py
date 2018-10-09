# -*-coding:utf-8 -*-
"""
Application's Forms

Ce programme est sous licence GNU GPL
©2017-2018 Nils et Samuel Van Zuijlen
"""
from django import forms
from django.core.validators import RegexValidator


PHONE_VALIDATOR = RegexValidator(
    regex=r'^(\+\d{1,2} \(0\)\d{9,15})|(\d{10})$',
    message="Le n° de téléphone doit être entré au format: '+84 (0)645564421'\
 ou '0654824178' (pour la France). Jusqu'à 15 chiffres autorisés."
    )


class AddUserForm(forms.Form):
    """create an user in a simple way"""

    lastname = forms.CharField(
        max_length=100,
        label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    firstname = forms.CharField(
        max_length=100,
        label="Prénom",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=100,
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Adresse mail du nouvel utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telephone = forms.CharField(
        validators=[PHONE_VALIDATOR],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    voluntary = forms.BooleanField(
        help_text="(Cochez si La personne souhaite être bénévole.)",
        label="Bénevole",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'})
    )
    addresses = forms.CharField(
        label="Adresse",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
