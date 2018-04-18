#!/usr/bin/env python

import pytest
import euler.fractions as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #d  Length of repeating cycle
        (2, 0),
        (3, 1),
        (5, 0),
        (7, 6),
    )

    return pairs


def test_cycle_length_prime(answers):
    for val, res in answers:
        assert eu.cycle_length_prime(val) == res



@pytest.fixture(scope="function")
def sqrt2():
    a0 = 1
    an = lambda x: 2

    return (a0, an)


def test_continued_fraction_denominator(sqrt2):
    a0, an = sqrt2

    assert eu.continued_fraction_denominator(0, a0, an) == 1
    assert eu.continued_fraction_denominator(1, a0, an) == 2
    assert eu.continued_fraction_denominator(2, a0, an) == 5
    assert eu.continued_fraction_denominator(3, a0, an) == 12
    assert eu.continued_fraction_denominator(4, a0, an) == 29


def test_continued_fraction_numerator(sqrt2):
    a0, an = sqrt2

    assert eu.continued_fraction_numerator(0, a0, an) == 1
    assert eu.continued_fraction_numerator(1, a0, an) == 3
    assert eu.continued_fraction_numerator(2, a0, an) == 7
    assert eu.continued_fraction_numerator(3, a0, an) == 17
    assert eu.continued_fraction_numerator(4, a0, an) == 41
