# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('testamento', models.CharField(blank=True, choices=[('1', 'Antiguo'), ('2', 'Nuevo')], max_length=2, null=True)),
            ],
            options={
                'db_table': 'libros',
            },
        ),
        migrations.CreateModel(
            name='Versiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bibla', models.PositiveIntegerField()),
                ('capitulo', models.PositiveIntegerField()),
                ('versiculo', models.PositiveIntegerField()),
                ('texto', models.CharField(max_length=500)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblia.Libros')),
            ],
            options={
                'db_table': 'versiculos',
            },
        ),
    ]
