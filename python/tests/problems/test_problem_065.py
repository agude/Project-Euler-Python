#!/usr/bin/env python

import pytest

from Problem065 import problem_065


def test_problem_065():
    assert problem_065(10) == 17
    assert problem_065() == 272
