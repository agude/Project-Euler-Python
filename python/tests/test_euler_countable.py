#!/usr/bin/env python

import pytest
import euler.countable as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #Number  Int     NonNeg  Pos     NonPos  Neg
        (1,      True,   True,   True,   False,  False),
        (1.,     True,   True,   True,   False,  False),
        (0,      True,   True,   False,  True,   False),
        (0.,     True,   True,   False,  True,   False),
        (-0.,    True,   True,   False,  True,   False),
        (-1,     True,   False,  False,  True,   True),
        (-1.,    True,   False,  False,  True,   True),
        (1.1,    False,  False,  False,  False,  False),
        (0.1,    False,  False,  False,  False,  False),
        (-1.1,   False,  False,  False,  False,  False),
    )

    return pairs


def test_is_integer(answers):
    for val, res, _, _, _, _ in answers:
        assert eu.is_integer(val) == res


def test_is_nonnegative_integer(answers):
    for val, _, res, _, _, _ in answers:
        assert eu.is_nonnegative_integer(val) == res


def test_is_positive_integer(answers):
    for val, _, _, res, _, _ in answers:
        assert eu.is_positive_integer(val) == res


def test_is_nonpositive_integer(answers):
    for val, _, _, _, res, _ in answers:
        assert eu.is_nonpositive_integer(val) == res


def test_is_negative_integer(answers):
    for val, _, _, _, _, res in answers:
        assert eu.is_negative_integer(val) == res
