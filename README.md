Tracker Project
=================

![Badge](https://img.shields.io/badge/python-2.7-green.svg)
![Badge](https://img.shields.io/badge/django-1.11.27-green.svg)
![Badge](https://img.shields.io/badge/postgresql-9.6-blue.svg)

Installation
================
```sh
$ git clone -repository.git-
$ cd tracker
$ rake setup:start
$ python manage.py runserver
```

Models
================
    Vehicle
    ________
        plate, Char
     
    NavigationRecord
    ________________
        vehicle,   FK(Vehicle)
        datetime,  Datetime
        latitude,  Float
        longitude, Float

Directory layout
================

Tracker's directory structure looks as follows::

    tracker/
    ├── tracker
    │   ├── __init__.py
    │   ├── settingsa.py
    │   ├── urls.py    
    │   ├── wsgi.py
    └── vehicle
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── utils.py
    │   │── migrations
    │   │   └── 0001.initial.py
    └── .gitignore
    └── manage.py
    └── README.md
    └── LICENCE
  

Licence
================
MIT