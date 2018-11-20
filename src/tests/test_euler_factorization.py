#!/usr/bin/env python

import pytest
import euler.factorization as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        (1, []),
        (2, [1]),
        (10, [1, 2, 5]),
        (10000, [1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 125, 200, 250, 400, 500, 625, 1000, 1250, 2000, 2500, 5000]),
        # Prime
        (472882027, [1]),
    )

    return pairs


def test_proper_factors(answers):
    for val, res in answers:
        assert eu.proper_factors(val) == res


def test_factors(answers):
    for val, res in answers:
        # The factors are the proper factors plus the number itself
        assert eu.factors(val) == res + [val]


def test_number_of_proper_factors(answers):
    for val, res in answers:
        assert eu.number_of_proper_factors(val) == len(res)


def test_number_of_factors(answers):
    for val, res in answers:
        # The factors are the proper factors plus the number itself
        assert eu.number_of_factors(val) == len(res) + 1
