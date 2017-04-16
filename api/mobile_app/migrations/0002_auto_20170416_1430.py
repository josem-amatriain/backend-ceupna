# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='timetable',
            field=models.CharField(blank=True, default='NoData', max_length=1000),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upna_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]