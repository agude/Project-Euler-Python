#!/usr/bin/env python

import pytest
import euler.dice as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #S    N   K    prop    under    over
        (1,   1,  1,   1.,     0.,      0.),
        (6,   1,  3,   1/6.,   2/6.,    3/6.),
        (6,   2,  7,   1/6.,   15/36.,  15/36.),
        (20,  1,  10,  1/20.,  9/20.,   10/20.),
        (2,   1,  3,   0,      1,       0),
    )

    return pairs


# From PEP 485
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def test_roll_probability(answers):
    for s, n, k, res, _, _ in answers:
        assert isclose(eu.roll_probability(s, n, k), res)


def test_roll_under_probability(answers):
    for s, n, k, _, res, _ in answers:
        assert isclose(eu.roll_under_probability(s, n, k), res)


def test_roll_over_probability(answers):
    for s, n, k, _, _, res in answers:
        assert isclose(eu.roll_over_probability(s, n, k), res)
