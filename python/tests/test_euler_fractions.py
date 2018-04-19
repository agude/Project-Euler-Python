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
    return eu.ContinuedFraction(a0, an)


def test_continued_fraction_denominator(sqrt2):
    assert sqrt2.nth_convergent_denominator(0) == 1
    assert sqrt2.nth_convergent_denominator(1) == 2
    assert sqrt2.nth_convergent_denominator(2) == 5
    assert sqrt2.nth_convergent_denominator(3) == 12
    assert sqrt2.nth_convergent_denominator(4) == 29


def test_continued_fraction_numerator(sqrt2):
    assert sqrt2.nth_convergent_numerator(0) == 1
    assert sqrt2.nth_convergent_numerator(1) == 3
    assert sqrt2.nth_convergent_numerator(2) == 7
    assert sqrt2.nth_convergent_numerator(3) == 17
    assert sqrt2.nth_convergent_numerator(4) == 41
