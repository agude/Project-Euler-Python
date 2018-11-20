#!/usr/bin/env python

import pytest
import euler.fibonacci as eu


@pytest.fixture(scope="function")
def answers():
    pairs = (
        #n F_n
        (0, 0),
        (1, 1),
        (70, 190392490709135),
        (500, 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125),
    )

    return pairs


def test_fibonacci(answers):
    for val, res in answers:
        assert eu.fibonacci(val) == res


def test_fibonaccis(answers):
    for val, res in answers:
        fibs = []
        for i in range(0, val + 1):
            fibs.append(eu.fibonacci(i))
        assert eu.fibonaccis(val) == fibs


def test_fibonacci_generator(answers):
    for val, res in answers:
        for i, fib in enumerate(eu.fibonacci_generator(val)):
            assert eu.fibonacci(i) == fib


def test_fibonacci_generator_with_mod(answers):
    for val, res in answers:
        for i, fib in enumerate(eu.fibonacci_generator(val, mod=10)):
            assert eu.fibonacci(i) % 10 == fib


def test_fibonacci_binet(answers):
    for val, res in answers:
        # Binet's formula is no longer accurate after n of 70
        if val <= 70:
            assert eu.fibonacci_binet(val) == res
