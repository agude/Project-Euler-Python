#!/usr/bin/env python

import pytest
import euler.pandigital as eu


def test_is_pandigital():
    pairs = (
        (0, False),
        (1, True),
        (10, False),
        (123456789, True),
        (912837465, True),
        (12837465, True),
        (1287465, False),
    )

    for val, res in pairs:
        assert eu.is_pandigital(val) is res


@pytest.mark.skip(reason="This test takes 4 seconds; run if changing pandigitals().")
def test_pandigitals():
    """Test that all number from pandigitals() are pandigital."""
    for test_num in eu.pandigitals():
        assert eu.is_pandigital(test_num)


def test_pandigitals_without_zero():
    """Test that pandigitals correctly generates all the 1, 2, and 3
    digit pandigitals when 0 is not included."""
    numbers = (1, 12, 21, 123, 132, 213, 231, 312, 321)
    pans = tuple(eu.pandigitals(1, 3))
    assert numbers == pans


def test_pandigitals_with_zero():
    """Test that pandigitals correctly generates all the 1, 2, and 3
    digit pandigitals when 0 is included."""
    numbers = (0, 1, 10, 12, 21, 102, 120, 123, 132, 201, 210, 213, 231, 312, 321)
    pans = tuple(eu.pandigitals(1, 3, True))
    assert numbers == pans
