# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-27 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediccion', '0009_auto_20181226_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextoHoroscopo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='horoscope',
            name='palabra',
            field=models.CharField(choices=[('AMOR', 'Amor'), ('TRABAJO', 'Trabajo'), ('SALUD', 'Salud')], default='AMOR', max_length=10),
        ),
        migrations.AlterField(
            model_name='horoscope',
            name='signo',
            field=models.CharField(choices=[('ARIES', 'ARIES'), ('TAURO', 'TAURO'), ('GEMINIS', 'GEMINIS'), ('CANCER', 'CANCER'), ('LEO', 'LEO'), ('VIRGO', 'VIRGO'), ('LIBRA', 'LIBRA'), ('ESCORPIO', 'ESCORPIO'), ('OFIUCO', 'OFIUCO'), ('SAGITARIO', 'SAGITARIO'), ('CAPRICORNIO', 'CAPRICORNIO'), ('ACUARIO', 'ACUARIO'), ('PISCIS', 'PISCIS')], default='ARIES', max_length=10),
        ),
    ]
