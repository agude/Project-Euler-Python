#!/usr/bin/env python

import pytest

from Problem005 import problem_005


def test_problem_005():
    assert problem_005(10) == 2520
    assert problem_005() == 232792560
