#!/bin/bash

cd helloworld/


# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate


# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput


#Start Unicorn Process
echo Starting Unicorn.

exec gunicorn helloworld.wsgi:application \
    --bind 0.0.0.0:8000\
    --workers 3