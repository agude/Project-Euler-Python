#!/usr/bin/env python

import pytest

from Problem104 import problem_104


@pytest.mark.skip(reason="Problem 104 takes about 10 seconds to complete.")
def test_problem_104():
    assert problem_104() == 329468
