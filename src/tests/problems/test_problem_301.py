#!/usr/bin/env python

import pytest

from Problem301 import problem_301


def test_problem_301_fast():
    assert problem_301(10_000_000) == 103_681

@pytest.mark.skip(reason="Problem 301 takes about 2 minutes to complete.")
def test_problem_301():
    assert problem_301() == 2_178_309
