#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
gunicorn IP_check.wsgi -b :8080
