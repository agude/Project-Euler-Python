#!/usr/bin/env python

import pytest

from Problem057 import problem_057


def test_problem_057():
    assert problem_057(7) == 0
    assert problem_057(8) == 1
    assert problem_057() == 153
