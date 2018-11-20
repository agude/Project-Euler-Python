#!/usr/bin/env python

import pytest

from Problem048 import problem_048


def test_problem_048():
    assert problem_048(10) == 405071317
    assert problem_048() == 9110846700
