# Project Euler in Python

Solutions to [Project Euler](https://projecteuler.net/) problems in Python.

## Usage

```bash
# Install dependencies
uv sync --all-extras

# Run a solution
uv run python src/Problem001.py

# Run tests
uv run pytest -v
```

## Structure

- `src/Problem*.py` - Problem solutions (Problem001.py, Problem002.py, ...)
- `src/euler/` - Shared math utilities (primes, fibonacci, factorization, etc.)
