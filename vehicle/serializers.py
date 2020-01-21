from datetime import datetime

__all__ = ['NavigationRecordSerializer']


class NavigationRecordSerializer(object):
    def __init__(self, queryset):
        self.queryset = queryset
        self._data = []

    @property
    def data(self):
        for obj in self.queryset:
            self._data.append({
                'latitude': obj.latitude,
                'longitude': obj.longitude,
                'vehicle_plate': obj.vehicle.plate,
                'datetime': datetime.strftime(obj.datetime, '%Y-%m-%d %H:%M:%S'),
            })
        return self._data
