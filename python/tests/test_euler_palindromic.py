#!/usr/bin/env python

import pytest
import euler.palindromic as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #Number  palindromic  binary_palindromic
        (1,      True,        True),
        (2,      True,        False),
        (-1,     True,        True),
        (-2,     True,        False),
        (15,     False,       True),
        (31,     False,       True),
        (-15,    False,       True),
        (-31,    False,       True),
        (11,     True,        False),
        (121,    True,        False),
        (-11,    True,        False),
        (-121,   True,        False),
    )

    return pairs


def test_is_palindromic(answers):
    for val, res, _ in answers:
        assert eu.is_palindromic(val) is res


def test_is_binary_palindromic(answers):
    for val, _, res in answers:
        assert eu.is_binary_palindromic(val) is res
