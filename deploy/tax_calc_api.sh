#!/usr/bin/env bash
set -e
source `poetry env info --path`/bin/activate
python manage.py runserver --settings=tax_calc_api.settings 0.0.0.0:80
