# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='classificacao',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
