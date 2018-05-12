# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=300)
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
