#!/bin/bash

#Start Unicorn Process
echo Starting Unicorn.

exec gunicorn helloworld.wsgi:application \
    --bind 0.0.0.0:8000\
    --workers 3