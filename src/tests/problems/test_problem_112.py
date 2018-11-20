#!/usr/bin/env python

import pytest

from Problem112 import problem_112


@pytest.mark.skip(reason="Problem 112 takes about 4 seconds to complete.")
def test_problem_112():
    assert problem_112() == 1587000
