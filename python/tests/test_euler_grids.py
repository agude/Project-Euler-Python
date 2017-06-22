#!/usr/bin/env python

import pytest
import euler.grids as eu


@pytest.fixture(scope="function")
def grid_2x2():
    return eu.Grid(["1 2", "03 04.1"])


def test_grid_2x2_structure(grid_2x2):
    g = grid_2x2
    assert g.rows == [[1, 2], [3, 4.1]]
    assert g.cols == [[1, 3], [2, 4.1]]
    assert g.backward_diagonals == [[2], [1, 4.1], [3]]
    assert g.forward_diagonals == [[1], [2, 3], [4.1]]


@pytest.fixture(scope="function")
def grid_3x2():
    return eu.Grid(["1 2 3", "04.1 05 6"])


def test_grid_3x2_structure(grid_3x2):
    g = grid_3x2
    assert g.rows == [[1, 2, 3], [4.1, 5, 6]]
    assert g.cols == [[1, 4.1], [2, 5], [3, 6]]
    assert g.backward_diagonals == [[3], [2, 6], [1, 5], [4.1]]
    assert g.forward_diagonals == [[1], [2, 4.1], [3, 5], [6]]


def test_grid_bad_rows():
    with pytest.raises(ValueError) as e_info:
        eu.Grid(["1", "2 3"])


def test_grid_bad_values():
    with pytest.raises(ValueError) as e_info:
        eu.Grid(["1 2", "duck 3"])


def test_grid_max_product():
    grid_start = (
        "99  0   0   99  0",
        "99  0   0   0   0",
        "0   99  0   0   0",
        "0   0   99  0   0",
        "99  99  99  99  99",
    )

    g = eu.Grid(grid_start)
    for i in range(1, 5):
        assert g.max_product(i) == 99**i


def test_grid_max_product_raise(grid_2x2):
    g = grid_2x2
    with pytest.raises(ValueError):
        g.max_product(0)
