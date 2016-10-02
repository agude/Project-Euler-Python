#!/usr/bin/env python

import pytest
import euler.combinatorics as eu


def test_n_choose_k():
    pairs = (
        (0, 0, 1),
        (1, 1, 1),
        (5, 3, 10),
        (54, 12, 343006888770),
        # k > n
        (0, 1, 0),
    )

    for n, k, res in pairs:
        assert eu.n_choose_k(n, k) == res
