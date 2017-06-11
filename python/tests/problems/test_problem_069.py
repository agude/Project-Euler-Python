#!/usr/bin/env python

import pytest

from Problem069 import problem_069


def test_problem_069():
    assert problem_069(10) == 6
    assert problem_069() == 510510
