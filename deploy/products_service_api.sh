#!/usr/bin/env bash
set -e
poetry install
source `poetry env info --path`/bin/activate
python manage.py migrate --settings=products_service_api.settings
python manage.py runserver --settings=products_service_api.settings 0.0.0.0:80
