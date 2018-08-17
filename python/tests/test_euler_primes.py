#!/usr/bin/env python

import pytest
import euler.primes as eu


@pytest.fixture(scope="function")
def primes():
    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
        191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
        257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
        331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
        401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    )

    return primes


def test_prime_sieve(primes):
    test = tuple(eu.prime_sieve(primes[-1] + 1))
    assert test == primes


def test_prime_sieve_float(primes):
    max_num = float(primes[-1] + 1) + 0.5
    test = tuple(eu.prime_sieve(max_num))
    assert test == primes


def test_primes(primes):
    test = []
    for prime in eu.primes():
        test.append(prime)
        if len(test) == len(primes):
            break

    assert tuple(test) == primes


def test_prime_factors():
    pairs = (
        (1, []),
        (100, [2, 2, 5, 5]),
        (137, [137]),
        (123345, [3, 3, 5, 2741])
    )

    for num, result in pairs:
        assert eu.prime_factors(num) == result


def test_is_prime(primes):
    for prime in primes:
        assert eu.is_prime(prime)


def test_circular_primes():
    pairs = (
        (1, []),
        (2, [2]),
        (1193, [1193, 1931, 9311, 3119]),
        (1234, []),
        (137, []),
    )

    primes = set(eu.prime_sieve(9312))
    for num, res in pairs:
        assert eu.circular_primes(num, prime_list=primes) == set(res)


@pytest.fixture(scope="function")
def truncatable_primes():
    left_primes = frozenset((
        2, 3, 5, 7, 13, 17, 23, 37, 43, 47, 53, 67, 73, 83, 97, 113,
        137, 167, 173, 197, 223, 283, 313, 317, 337, 347, 353, 367,
        373, 383, 397, 443, 467, 523, 547, 613, 617, 643, 647, 653,
        673, 683, 743, 773, 797, 823, 853, 883, 937, 947, 953, 967,
        983, 997, 1223,
    ))
    right_primes = frozenset((
        2, 3, 5, 7, 23, 29, 31, 37, 53, 59, 71, 73, 79, 233, 239, 293,
        311, 313, 317, 373, 379, 593, 599, 719, 733, 739, 797,
    ))

    return (left_primes, right_primes)


@pytest.fixture(scope="function")
def right_truncatable_primes():

    return primes


def test_is_truncatable_prime_left(truncatable_primes):
    left, right = truncatable_primes
    for prime in left:
        assert eu.is_truncatable_prime(prime)

    not_left = right - left
    for prime in not_left:
        assert not eu.is_truncatable_prime(prime)


def test_is_left_truncatable_prime(truncatable_primes):
    left, right = truncatable_primes
    for prime in left:
        assert eu.is_left_truncatable_prime(prime)

    not_left = right - left
    for prime in not_left:
        assert not eu.is_left_truncatable_prime(prime)


def test_is_truncatable_prime_right(truncatable_primes):
    left, right = truncatable_primes
    for prime in right:
        assert eu.is_truncatable_prime(prime, right_truncate=True)

    not_right = left - right
    for prime in not_right:
        assert not eu.is_truncatable_prime(prime, right_truncate=True)


def test_is_right_truncatable_prime(truncatable_primes):
    left, right = truncatable_primes
    for prime in right:
        assert eu.is_right_truncatable_prime(prime)

    not_right = left - right
    for prime in not_right:
        assert not eu.is_right_truncatable_prime(prime)


def test_is_two_sided_prime(truncatable_primes):
    left, right = truncatable_primes
    both = left.intersection(right)

    for prime in both:
        assert eu.is_two_sided_prime(prime)

    neither = left.symmetric_difference(right)
    for prime in neither:
        assert not eu.is_two_sided_prime(prime)


def test_are_coprime(primes):
    # 1 and 1 are coprime
    assert eu.are_coprime(1, 1)

    # 2 and 2 are not coprime
    assert eu.are_coprime(2, 2) is False

    # Any number and 1 are coprime
    for i in range(100):
        assert eu.are_coprime(1, i)

    # Any odd number is coprime to 2
    for i in range(3, 100, 2):
        assert eu.are_coprime(2, i)

    # All primes are coprime to each other
    for i, prime_i in enumerate(primes):
        for j in range(i+1, len(primes)):
            prime_j = primes[j]
            assert eu.are_coprime(prime_i, prime_j)
