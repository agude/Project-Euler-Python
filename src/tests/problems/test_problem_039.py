#!/usr/bin/env python

import pytest

from Problem039 import problem_039


@pytest.mark.skip(reason="Problem 39 takes 10 seconds to complete.")
def test_problem_039():
    assert problem_039() == 840
