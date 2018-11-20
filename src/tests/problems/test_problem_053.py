#!/usr/bin/env python

import pytest

from Problem053 import problem_053


def test_problem_053():
    assert problem_053(23) == 4
    assert problem_053() == 4075
