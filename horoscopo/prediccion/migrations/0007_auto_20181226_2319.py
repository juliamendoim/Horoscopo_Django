# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-27 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediccion', '0006_auto_20181226_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horoscope',
            name='Temas',
            field=models.CharField(choices=[('Amor', 'Amor'), ('Salud', 'Salud'), ('Trabajo', 'Trabajo')], default='Bueh', max_length=1),
        ),
    ]
