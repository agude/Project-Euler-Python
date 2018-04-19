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

def test_sort_digits():
    assert eu.sort_digits(100) == 100
    assert eu.sort_digits(10) == 10
    assert eu.sort_digits(0) == 0
    assert eu.sort_digits(1) == 1
    assert eu.sort_digits(12345) == 54321


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


def test_NumberWriter():
    pairs = (
        (0, "zero"),
        (1, "one"),
        (10, "ten"),
        (11, "eleven"),
        (57, "fifty-seven"),
        (100, "one hundred"),
        (1000, "one thousand"),
        (1234, "one thousand two hundred and thirty-four"),
        (10000, "ten thousand"),
        (100000, "one hundred thousand"),
        (1000000, "one million"),
        (1000000000, "one billion"),
        (1234567890, "one billion two hundred and thirty-four million five hundred and sixty-seven thousand eight hundred and ninety"),
    )

    for number, result in pairs:
        n = eu.NumberWriter(number)
        assert n.word == result


def test_NumberWriter_raises():
    with pytest.raises(ValueError) as e_info:
        n = eu.NumberWriter(-1)
