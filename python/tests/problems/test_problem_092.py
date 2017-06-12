#!/usr/bin/env python

import pytest

from Problem092 import problem_092


def test_problem_092_fast():
    assert problem_092(1000) == 857


@pytest.mark.skip(reason="Problem 92 takes 40 seconds to complete.")
def test_problem_092():
    assert problem_092() == 8581146
