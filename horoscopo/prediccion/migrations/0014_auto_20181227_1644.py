# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-27 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediccion', '0013_auto_20181227_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]
