# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 20:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_semester',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
