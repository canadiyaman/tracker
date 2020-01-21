# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.utils import timezone

from .models import NavigationRecord
from .serializers import NavigationRecordSerializer

__all__ = ['get_last_points']


def get_last_points():
    queryset = NavigationRecord.objects.filter(datetime__gte=timezone.now() - timedelta(hours=48))
    return NavigationRecordSerializer(queryset).data
