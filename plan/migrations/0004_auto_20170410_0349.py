# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20170410_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorroadmaps',
            name='major',
            field=models.CharField(max_length=200),
        ),
    ]