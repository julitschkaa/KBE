#!/usr/bin/env bash
set -e
poetry install
source `poetry env info --path`/bin/activate

while true
do
	#python manage.py export_csv --settings=products_service_api.settings
	python import_csv.py
	sleep 10 #alle 10 Sekunden
done