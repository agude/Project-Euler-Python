#!/usr/bin/env python

import pytest

from Problem017 import problem_017


def test_problem_017_fast():
    assert problem_017(5) == 19

def test_problem_017():
    assert problem_017() == 21124
