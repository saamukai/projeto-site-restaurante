#!/bin/bash

echo "Make migrations"
python3 manage.py makemigrations --noinput

echo "Apply database migrations"
python3 manage.py migrate --fake-initial --noinput

echo "Load fixtures json"
python3 manage.py loaddata core/fixtures/*.json

python3 manage.py runserver 0.0.0.0:3000
