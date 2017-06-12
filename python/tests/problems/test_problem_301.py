#!/usr/bin/env python

import pytest

from Problem301 import problem_301


@pytest.mark.skip(reason="Problem 301 takes about 2 minutes to complete.")
def test_problem_301():
    assert problem_301() == 2178309
