#!/usr/bin/env python

import pytest
import euler.digits as eu


def test_square_and_add():
    PAIRS = (
        (0, 0), (1, 1), (2, 4), (10, 1), (21, 5), (44, 32), (32, 13), (85, 89),
        (145, 42), (42, 20), (20, 4), (4, 16), (16, 37), (37, 58), (37, 58),
        (58, 89),
    )

    for val, answer in PAIRS:
        assert eu.square_and_add(val) == answer


def test_valueerror():
    for value in (-1, 1.5, -1.5):
        with pytest.raises(ValueError) as e_info:
            eu.square_and_add(value)
