#!/usr/bin/env python

import pytest

from Problem059 import problem_059


@pytest.mark.skip(reason="Problem 59 takes about 5 seconds to complete.")
def test_problem_059():
    assert problem_059() == 107359
