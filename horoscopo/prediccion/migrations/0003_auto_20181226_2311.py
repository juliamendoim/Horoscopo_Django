# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-27 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediccion', '0002_horoscope_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horoscope',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='horoscope',
            name='palabra',
        ),
        migrations.AddField(
            model_name='horoscope',
            name='Temas',
            field=models.CharField(choices=[('Amor', 'Amor'), ('Salud', 'Salud'), ('Trabajo', 'Trabajo')], default='Amor', max_length=1),
        ),
    ]