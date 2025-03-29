#!/usr/bin/env bash
set -o errexit

# Upgrade pip using python's module invocation
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
