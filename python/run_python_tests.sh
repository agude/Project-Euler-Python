#!/bin/bash

python3 -m pytest -v
echo "Running mypy type testing"
python3 -m mypy --ignore-missing-imports ./Problem*.py
