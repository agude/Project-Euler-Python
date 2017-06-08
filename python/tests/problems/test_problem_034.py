#!/usr/bin/env python

import pytest

from Problem034 import problem_034


@pytest.mark.skip(reason="Problem 34 takes 8 seconds to complete.")
def test_problem_034():
    assert problem_034() == 40730
