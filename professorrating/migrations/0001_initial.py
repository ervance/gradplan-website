# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=10)),
                ('class_id', models.IntegerField(blank=True)),
                ('number_rating', models.IntegerField(blank=True)),
                ('rating', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('average_rating', models.IntegerField(blank=True, default=0)),
                ('number_of_ratings', models.IntegerField(blank=True, default=0)),
                ('total_rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AddField(
            model_name='classrating',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professorrating.Professor'),
        ),
    ]
