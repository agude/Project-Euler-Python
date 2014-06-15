#!/usr/bin/env python3

#  Copyright (C) 2014  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  The most recent version of this program is available at:
#  https://github.com/agude/Project-Euler

""" It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2x1**2
15 = 7 + 2x2**2
21 = 3 + 2x3**2
25 = 7 + 2x3**2
27 = 19 + 2x2**2
33 = 31 + 2x1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from math import sqrt
from euler.countable import is_integer


def is_counterexample(number, primes):
    """
    Checks if a number is a counterexample to Goldbach's other conjecture.

    Goldbach's other conjecture states that every odd composite is the sum of a
    prime and twice the square of a number.

    This function takes a number to test, and a list of all the primes smaller
    than that number, and checks the following formula for every prime:

    c = sqrt((number - prime) / 2)

    If c is an integer, then we have not found a counterexample, but if we
    exhaust all of the primes without finding c as an integer then we have a
    counter example.

    Args:
        number (int): The number to check.
        primes (list): A list of all prime numbers smaller than number.

    Returns:
        bool: True if number is a counterexample, False otherwise.
    """
    # Primes are not odd composites
    if number in primes:
        return False
    # Even numbers are not odd composites
    if not number % 2:
        return False
    # We try to divide by every prime number smaller than our composite, if we
    # find one such that (sqrt(composite - prime) / 2) is an integer, then we
    # have NOT found a counter example.
    for prime in primes:
        if prime < number:
            test_number = sqrt((number - prime) / 2)
            if is_integer(test_number):
                return False
    # At this point we have exhausted all tests, and the number is an odd
    # composite, but does not follow Goldbach's other conjecture and hence is a
    # counter example.
    return True


# Only runs if executed directly
if __name__ == '__main__':
    from euler.converter import int_to_tuple
    from euler.primes import primes
    from time import time
    from sys import exit

    # Solution
    start_time = time()

    last_prime = 2
    prime_list = []
    # We loop over primes and find all the composite numbers between them. We
    # then check if these are counter examples to the conjecture with
    # is_counterexample.
    for prime in primes():
        prime_list.append(prime)
        for composite in range(last_prime + 1, prime):
            if is_counterexample(composite, prime_list):
                end_time = time() - start_time
                print(composite, 'in', end_time, 'secs')
                exit()
        # No counter example yet, move on to the next prime and set the current
        # one to the lower bound.
        last_prime = prime
