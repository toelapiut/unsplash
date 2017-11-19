# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 16:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='photo_three',
            field=models.ImageField(default=datetime.datetime(2017, 11, 18, 16, 22, 49, 982062, tzinfo=utc), upload_to='articles/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photos',
            name='photo_two',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
