#!/bin/bash

python3 -m pytest -v
python3 -m mypy --ignore-missing-imports ./Problem*.py
