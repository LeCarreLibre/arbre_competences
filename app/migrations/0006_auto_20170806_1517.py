# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170726_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profil', verbose_name='utilisateur concerné'),
        ),
    ]