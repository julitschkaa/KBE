#!/usr/bin/env bash
set -e
source .env
poetry install
source `poetry env info --path`/bin/activate
echo "---starting unit tests of tax-calc---"
pytest tax_calc/tax_calculator_unit_tests.py
echo "---starting integration Tests---"
export MANGODB2_USERNAME=$MANGO2_INITDB_ROOT_USERNAME
export MANGODB2_PASSWORD=$MANGO2_INITDB_ROOT_PASSWORD
pytest integration_tests.py