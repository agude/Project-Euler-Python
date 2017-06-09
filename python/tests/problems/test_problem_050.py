#!/usr/bin/env python

import pytest

from Problem050 import problem_050


def test_problem_050():
    assert problem_050(100) == 41
    assert problem_050(1000) == 953
    assert problem_050() == 997651
