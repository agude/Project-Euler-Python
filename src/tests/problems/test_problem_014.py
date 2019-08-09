#!/usr/bin/env python

import pytest

from Problem014 import problem_014


def test_problem_014_fast():
    assert problem_014(20) == 19
    assert problem_014(1000) == 871

def test_problem_014():
    assert problem_014() == 837_799
