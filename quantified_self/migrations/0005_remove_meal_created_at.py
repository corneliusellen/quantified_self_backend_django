# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quantified_self', '0004_auto_20180517_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='created_at',
        ),
    ]
