#!/usr/bin/env python

import pytest
import numpy as np
import euler.converter as eu


def test_iterable_to_int():
    pairs = (
        ((1, 2, 3), 123),
        (("1", "2", "3"), 123),
        ((1,), 1),
        (("1",), 1),
        ([1, 2, 3], 123),
        (["1", "2", "3"], 123),
        ([1], 1),
        (["1"], 1),
        (np.array((1, 2, 3)), 123),
        (np.array(("1", "2", "3")), 123),
        (np.array((1,)), 1),
        (np.array(("1",)), 1),
    )

    for val, res in pairs:
        assert eu.iterable_to_int(val) == res


def test_int_to_tuple():
    pairs = (
        (123, (1, 2, 3)),
        (1, (1,)),
    )

    for val, res in pairs:
        assert eu.int_to_tuple(val) == res


def test_truncate():
    pairs = (
        # Number Right_Truncate Answer
        (-12, False, -2),
        (-12, True, -1),
        (12, False, 2),
        (12, True, 1),
        (-1, False, None),
        (1, False, None),
        (-1, True, None),
        (1, True, None),
    )
    for val, rt, res in pairs:
        assert eu.truncate(val, right_truncate=rt) == res
        # Test Aliases
        if rt:
            assert eu.right_truncate(val) == res
        else:
            assert eu.left_truncate(val) == res


def test_int_to_tuple():
    pairs = (
        (-123, -321),
        (123, 321),
        (1, 1),
        (-0, 0),
    )

    for val, res in pairs:
        assert eu.reverse_int(val) == res
