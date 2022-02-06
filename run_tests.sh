#!/usr/bin/env bash
set -e
poetry install
source `poetry env info --path`/bin/activate
echo "---starting unit tests of tax-calc---"
pytest tax_calc/tax_calculator_unit_tests.py
echo "---starting integration Tests---"
pytest integration_tests.py