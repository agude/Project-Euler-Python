#!/usr/bin/env python

import pytest

from Problem024 import problem_024


def test_problem_024():
    assert problem_024() == "2783915460"
    assert problem_024(1, [0, 1]) == "01"
    assert problem_024(2, [0, 1]) == "10"
