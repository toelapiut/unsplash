# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]