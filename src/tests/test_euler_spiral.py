#!/usr/bin/env python

import pytest
import euler.spiral as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #Size Sum
        (5, 101),
    )

    return pairs


def test_spiral_sum(answers):
    for val, res in answers:
        sp = eu.Spiral(val)
        assert sp.sum == res


def test_spiral_raise():
    # Even values are not allowed
    for n in range(0, 10, 2):
        with pytest.raises(ValueError) as e_info:
            eu.Spiral(n)
