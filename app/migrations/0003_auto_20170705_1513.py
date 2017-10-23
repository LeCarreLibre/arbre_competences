# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170705_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='categorie',
        ),
        migrations.AddField(
            model_name='detail',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Categorie'),
            preserve_default=False,
        ),
    ]