# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-27 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediccion', '0005_auto_20181226_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horoscope',
            name='Temas',
            field=models.CharField(choices=[('Amor', 'Amor'), ('Salud', 'Salud'), ('Trabajo', 'Trabajo')], default='None', max_length=1),
        ),
    ]
