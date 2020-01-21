# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import Vehicle, NavigationRecord
from .utils import get_last_points


def get_random_plate(v):
    return '{0} {1} {2}'.format(
        ('0%d' % v)[:2],
        ''.join(random.choice(string.ascii_uppercase) for _ in range(3)),
        ('0%d' % v)[:2]
    )


def create_random_data():
    for v in range(100):
        vehicle = Vehicle.objects.create(plate=get_random_plate(v))
        for nr in range(10):
            NavigationRecord.objects.create(
                vehicle=vehicle,
                latitude=random.uniform(10.5, 100.5),
                longitude=random.uniform(10.5, 100.5)
            )


class VehicleTestCase(TestCase):
    def test_crud_vehicle(self):
        # create
        vehicle = Vehicle.objects.create(plate='00 ABC 99')
        self.assertEqual(vehicle.pk, vehicle.id)

        # read
        queryset = Vehicle.objects.all()
        self.assertQuerysetEqual(queryset, ['<Vehicle: 00 ABC 99>'])

        # update
        vehicle.plate = '99 XYZ 000'
        vehicle.save()
        updated_vehicle = Vehicle.objects.last()
        self.assertEqual(updated_vehicle.plate, '99 XYZ 000')

        # delete
        deleted = Vehicle.objects.last().delete()
        self.assertEqual(deleted, (1, {u'vehicle.NavigationRecord': 0, u'vehicle.Vehicle': 1}))


class NavigationRecordTestCase(TestCase):
    def test_crud_navigation_record(self):
        # create
        vehicle = Vehicle.objects.create(plate='00 ABC 99')
        data = {
            'vehicle': vehicle,
            'latitude': 32.32,
            'longitude': 32.32
        }
        navigation_record = NavigationRecord.objects.create(**data)
        self.assertEqual(navigation_record.pk, navigation_record.id)

        # read
        navigation_record_list = list(NavigationRecord.objects.all().values_list('vehicle__plate', flat=True))
        self.assertEqual(navigation_record_list, ['00 ABC 99'])

        # update
        updated_vehicle = Vehicle.objects.create(plate='99 XYZ 000')
        navigation_record.vehicle = updated_vehicle
        navigation_record.save()
        updated_navigation_record_list = list(NavigationRecord.objects.all().values_list('vehicle__plate', flat=True))
        self.assertEqual(updated_navigation_record_list, ['99 XYZ 000'])

        # delete
        deleted = NavigationRecord.objects.last().delete()
        self.assertEqual(deleted, (1, {u'vehicle.NavigationRecord': 1}))

    def test_get_last_points_function(self):
        create_random_data()

        self.assertEqual(Vehicle.objects.count(), 100)
        self.assertEqual(NavigationRecord.objects.count(), 1000)
        data = get_last_points()
        self.assertEqual(len(data), 1000)

    def test_get_last_points_function_with_manipulated_date(self):
        create_random_data()

        # navigation record which is creted before than 48 hours
        vehicle = Vehicle.objects.last()
        navigation_record = NavigationRecord.objects.create(
            vehicle=vehicle,
            latitude=32.32,
            longitude=32.32
        )
        navigation_record.datetime = timezone.now() - timedelta(hours=72)
        navigation_record.save()

        data = get_last_points()
        self.assertEqual(len(data), 1000)
