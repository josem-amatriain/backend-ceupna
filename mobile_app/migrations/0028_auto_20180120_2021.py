# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0027_auto_20180114_0624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentcouncil',
            options={'ordering': ('center', 'created'), 'verbose_name': 'Consejo de Estudiantes', 'verbose_name_plural': 'Consejos de Estudiantes'},
        ),
        migrations.AlterField(
            model_name='responsibility',
            name='representative',
            field=models.ManyToManyField(related_name='responsibility_representatives', related_query_name='rres', through='mobile_app.ResponsibilityRepresentativeHistory', to='mobile_app.Representative'),
        ),
        migrations.AlterField(
            model_name='studentcouncil',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mobile_app.Center'),
        ),
    ]
