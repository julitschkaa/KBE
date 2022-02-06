#!/usr/bin/env bash
set -e
poetry install
source `poetry env info --path`/bin/activate
pytest
echo "---starting integration Tests---"
docker-compose up -d
sleep 100

curl localhost/tax-calculator/
curl localhost/products/
curl localhost/tax-calculator/?cent=100

docker-compose down