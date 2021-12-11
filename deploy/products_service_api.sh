#!/usr/bin/env bash
set -e
git clone /app
cd app
source `poetry env info --path`/bin/activate
python manage.py runserver --settings=products_service_api.settings --port=80
