# -*- coding: utf-8 -*-
"""
This file was not generated by Django!
©2019 Samuel Van Zuijlen
"""
from django.conf import settings
from django.db import migrations


def forwards(apps, _):
    """ Récupèration des données et écriture de la table """
    try:
        OldModel = apps.get_model('competences', 'Profil')
    except LookupError:
        print('Erreur l\'ancienne application n\'est pas installé')
        return
    NewModel = apps.get_model('utilisateurs', 'Profil')
    NewModel.objects.bulk_create(
        NewModel(new_attribute=old_object.old_attribute)
        # Attention! old_attribute n'existe pas pour old_object(Profil) une
        # erreur peut survenir
        for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):
    """ Apply the migration """

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competences', '0001_initial'),
        ('utilisateurs', '0001_profil'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
