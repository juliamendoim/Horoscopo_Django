# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-27 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prediccion', '0011_delete_textohoroscopo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='horoscope',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='prediccion.Usuario'),
        ),
    ]
