# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-31 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umbrella', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_department',
            name='technology1',
            field=models.CharField(default='SOME STRING', max_length=40),
        ),
    ]