#!/usr/bin/env python

import pytest

from Problem145 import problem_145


def test_problem_145_fast():
    assert problem_145(1000) == 120


@pytest.mark.skip(reason="Problem 145 takes over 40 minutes to complete.")
def test_problem_145():
    assert problem_145() == 608720
