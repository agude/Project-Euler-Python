#!/usr/bin/env python

import pytest
import euler.bouncy as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #Number           NumberSlope                 Decreasing  Increasing  Bouncy
        (1,               eu.NumberSlope.both,        True,       True,       False),
        (9876543210,      eu.NumberSlope.decreasing,  True,       False,      False),
        (99999876543210,  eu.NumberSlope.decreasing,  True,       False,      False),
        (123456789,       eu.NumberSlope.increasing,  False,      True,       False),
        (1111123456789,   eu.NumberSlope.increasing,  False,      True,       False),
        (90909090,        eu.NumberSlope.bouncy,      False,      False,      True),
        (909,             eu.NumberSlope.bouncy,      False,      False,      True),
    )

    return pairs


def test_slope(answers):
    for val, res, _, _, _ in answers:
        assert eu.check_number_slope(val) is res


def test_is_decreasing(answers):
    for val, _, res, _, _ in answers:
        assert eu.is_decreasing(val) == res


def test_is_increasing(answers):
    for val, _, _, res, _ in answers:
        assert eu.is_increasing(val) == res


def test_is_bouncy(answers):
    for val, _, _, _, res in answers:
        assert eu.is_bouncy(val) == res
