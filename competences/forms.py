from django import forms


class AddUserForm(forms.Form):
    """create a user with a simple way"""

    lastname = forms.CharField(max_length=100, label="Nom")
    firstname = forms.CharField(max_length=100, label="Prénom")
    username = forms.CharField(max_length=100, label="Nom d'utilisateur")
    email = forms.EmailField(label="Votre adresse mail")
    telephone = forms.CharField(min_length=10, max_length=15)
    voluntary = forms.BooleanField(help_text="Cochez si vous souhaitez être "
                                             "bénévole.", label="Bénevole", required=False)
    addresses = forms.CharField(label="Adresse")
