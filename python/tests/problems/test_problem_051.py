#!/usr/bin/env python

import pytest

from Problem051 import problem_051


@pytest.mark.skip(reason="Problem 51 takes about 30 seconds to complete.")
def test_problem_051():
    assert problem_051() == 121313
