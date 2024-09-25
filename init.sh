#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py rebuild_index
python manage.py runserver