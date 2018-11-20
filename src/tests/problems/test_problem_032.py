#!/usr/bin/env python

import pytest

from Problem032 import problem_032


@pytest.mark.skip(reason="Problem 32 takes over a minute to complete.")
def test_problem_032():
    assert problem_032() == 45228
