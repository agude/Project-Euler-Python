#!/usr/bin/env python

import pytest
import euler.graphs as eu


@pytest.fixture(scope="function")
def pyramid():
    tup = ((3,), (7, 4), (2, 4, 6), (8, 5, 9, 3))
    string = "3\n7 4\n2 4 6\n8 5 9 3"
    pg = eu.PyramidGraph(tup)

    return (pg, 23, tup, string)


def test_largest_sum(pyramid):
    graph = pyramid[0]
    largest_sum = pyramid[1]
    assert graph.largest_sum() == largest_sum


def test_getitem(pyramid):
    graph = pyramid[0]
    tup = pyramid[2]
    for i in range(len(tup)):
        assert graph[i] == tup[i]


def test_len(pyramid):
    graph = pyramid[0]
    tup = pyramid[2]
    assert len(graph) == len(tup)


def test_repr(pyramid):
    graph = pyramid[0]
    tup = pyramid[2]
    assert repr(graph) == repr(tup)


def test_str(pyramid):
    graph = pyramid[0]
    string = pyramid[3]
    assert str(graph) == string
