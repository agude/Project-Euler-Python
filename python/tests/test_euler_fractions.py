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
