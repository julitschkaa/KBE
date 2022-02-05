#!/usr/bin/env bash
set -e
poetry install
source `poetry env info --path`/bin/activate

while true
do
	python import_csv.py
	sleep 10 #every 10 seconds the csv file ist downloaded from the sftp server and then put into Mangodb2
done