# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

__all__ = ['Vehicle', 'NavigationRecord']


class Vehicle(models.Model):
    plate = models.CharField(max_length=255)

    def __str__(self):
        return self.plate

    class Meta:
        app_label = 'vehicle'
        verbose_name = 'vehicles'
        verbose_name_plural = 'vehicles'


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE, related_name='navigation_records')
    datetime = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return '%s - %s' % (self.vehicle, datetime.strftime(self.datetime, '%Y-%m-%d %H:%M:%S'))

    class Meta:
        app_label = 'vehicle'
        verbose_name = 'navigation record'
        verbose_name_plural = 'navigation records'
