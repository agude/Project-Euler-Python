#!/usr/bin/env python

import pytest

from Problem206 import problem_206


@pytest.mark.skip(reason="Problem 206 takes about 20 seconds to complete.")
def test_problem_206():
    assert problem_206() == 1389019170
