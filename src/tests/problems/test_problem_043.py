#!/usr/bin/env python

import pytest

from Problem043 import problem_043


@pytest.mark.skip(reason="Problem 43 takes 45 seconds to complete.")
def test_problem_043():
    assert problem_043() == 16695334890
