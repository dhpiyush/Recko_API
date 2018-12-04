# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-02 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recko_api', '0004_person_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='family_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='universe',
            name='universe_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]