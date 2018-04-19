#!/usr/bin/env python

import pytest
import euler.polygonal as eu


@pytest.fixture(scope="function")
def triangles():
    triangles = (
        0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120,
        136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378,
        406,
    )

    return triangles


def test_is_triangular(triangles):
    for num in triangles:
        assert eu.is_triangular(num)


def test_triangulars(triangles):
    stop = len(triangles) - 1
    test = tuple(eu.triangulars(stop, start=0))
    assert test == triangles


@pytest.fixture(scope="function")
def pentagons():
    pents = (
        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287,
        330, 376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001,
    )

    return pents


def test_is_pentagonal(pentagons):
    for num in pentagons:
        assert eu.is_pentagonal(num)


def test_pentagonals(pentagons):
    stop = len(pentagons)
    test = tuple(eu.pentagonals(stop))
    assert test == pentagons


@pytest.fixture(scope="function")
def hexagons():
    hexes = (
        1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378,
        435, 496, 561, 630, 703, 780, 861, 946,
    )

    return hexes


def test_is_pentagonal(hexagons):
    for num in hexagons:
        assert eu.is_hexagonal(num)


def test_pentagonals(hexagons):
    stop = len(hexagons)
    test = tuple(eu.hexagonals(stop))
    assert test == hexagons


@pytest.fixture(scope="function")
def squares():
    squares = (0, 1, 4, 9, 16, 25)

    return squares


def test_squares(squares):
    stop = len(squares) - 1
    test = tuple(eu.squares(stop, start=0))
    assert test == squares


@pytest.fixture(scope="function")
def heptagonals():
    heptagonals = (0, 1, 7, 18, 34, 55)

    return heptagonals


def test_heptagonals(heptagonals):
    stop = len(heptagonals) - 1
    test = tuple(eu.heptagonals(stop, start=0))
    assert test == heptagonals


@pytest.fixture(scope="function")
def octagonals():
    octagonals = (0, 1, 8, 21, 40, 65)

    return octagonals


def test_octagonals(octagonals):
    stop = len(octagonals) - 1
    test = tuple(eu.octagonals(stop, start=0))
    assert test == octagonals
