# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hermanos', '0002_hermanos_user'),
        ('culto', '0009_auto_20160520_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultos',
            name='escuela_dominical',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='escuela_dominical', to='hermanos.Hermanos'),
        ),
    ]