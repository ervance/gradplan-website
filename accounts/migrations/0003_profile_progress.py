# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170416_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='progress',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
