# CLAUDE.md

This file provides guidance to agents when working with code in this repository.

## Project Overview

Python solutions to Project Euler problems with a reusable utility library.

## Commands

Install dependencies:
```bash
uv sync --all-extras
```

Run all tests:
```bash
uv run pytest -v
```

Run a single test file:
```bash
uv run pytest -v src/tests/test_euler_primes.py
uv run pytest -v src/tests/problems/test_problem_001.py
```

Type checking:
```bash
uv run mypy src/Problem*.py src/euler/*.py
```

Run a specific problem solution:
```bash
uv run python src/Problem001.py
uv run python src/Problem001.py -n 100  # with custom argument
```

## Architecture

### Problem Solutions (`src/Problem*.py`)

Each problem is a standalone script with:
- A `problem_NNN()` function that returns the answer
- Command-line argument parsing via `optparse`
- Built-in timing output

### Utility Library (`src/euler/`)

Reusable mathematical functions imported by problem solutions:

- `primes.py` - Prime number generation (sieve, generator), primality tests, factorization
- `fibonacci.py` - Fibonacci sequence generation
- `polygonal.py` - Triangle, pentagonal, hexagonal numbers
- `totient.py` - Euler's totient function
- `factorization.py` - Factor finding
- `converter.py` - Number/string/tuple conversions
- `pandigital.py` - Pandigital number utilities
- `palindromic.py` - Palindrome detection
- `combinatorics.py` - Permutations and combinations
- `cards.py` - Playing card representation for poker problems
- `graphs.py` - Graph algorithms
- `grids.py` - 2D grid operations

### Tests (`src/tests/`)

- `tests/test_euler_*.py` - Unit tests for the euler library
- `tests/problems/test_problem_*.py` - Regression tests that verify each problem returns the correct answer

