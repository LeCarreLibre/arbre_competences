# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import migrations
from django.apps import apps as global_apps
import django.db.models.deletion

def forwards(apps, schema_editor):
    try:
        OldModel = apps.get_model('competences', 'Profil')
    except LookupError:
        print('Erreur l\'ancienne application n\'est pas installé')
        return
    NewModel = apps.get_model('utilisateurs', 'Profil')
    NewModel.objects.bulk_create(
        NewModel(new_attribute=old_object.old_attribute)
        # Attention! old_attribute n'existe pas pour old_object(Profil) une erreur peut survenir
        for old_object in OldModel.objects.all()
    )

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competences', '0002_auto_20180410_2311'),
        ('utilisateurs', '0001_profil'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
