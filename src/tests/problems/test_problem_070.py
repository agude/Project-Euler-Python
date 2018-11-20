#!/usr/bin/env python

import pytest

from Problem070 import problem_070


@pytest.mark.skip(reason="Problem 70 takes about 2 minutes to complete.")
def test_problem_070():
    assert problem_070() == 8319823
