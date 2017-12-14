from django import forms


class NewUser(forms.Form):
    """create a user with a simple way"""

    lastname = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(label="Votre adresse mail")
    telephone = forms.CharField(min_length=10, max_length=15)
    voluntary = forms.BooleanField(help_text="Cochez si vous souhaitez être "
                                             "bénévole.", required=False)
    addresses = forms.CharField()
