#!/usr/bin/env python

import pytest

from Problem072 import problem_072


@pytest.mark.skip(reason="Problem 72 takes about 5 seconds to complete.")
def test_problem_072():
    assert problem_072() == 303963552391
