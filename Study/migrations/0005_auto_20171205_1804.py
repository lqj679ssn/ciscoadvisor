# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0004_auto_20171204_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='iteration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trail',
            name='metric',
            field=models.FloatField(),
        ),
    ]
