# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantified_self', '0003_meal_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]