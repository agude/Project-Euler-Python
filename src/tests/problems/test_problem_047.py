#!/usr/bin/env python

import pytest

from Problem047 import problem_047


def test_problem_047_fast():
    assert problem_047(1) == 2
    assert problem_047(2) == 14
    assert problem_047(3) == 644


@pytest.mark.skip(reason="Problem 47 takes about 5 minutes to complete.")
def test_problem_047():
    assert problem_047(4) == 134043
