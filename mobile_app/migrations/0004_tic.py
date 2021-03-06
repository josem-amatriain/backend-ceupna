# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0003_auto_20170416_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='TIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('icon', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('link', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
