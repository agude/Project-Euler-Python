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

"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2  =   0.5
    1/3  =   0.(3)
    1/4  =   0.25
    1/5  =   0.2
    1/6  =   0.1(6)
    1/7  =   0.(142857)
    1/8  =   0.125
    1/9  =   0.(1)
    1/10 =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""

from euler.countable import is_positive_integer


# Functions
def cycle_length(number):
    """ Return the length of cycle of repeating digits of 1/number.

    This function uses the fact that, for certain primes, the length is equal
    to p where ((10 ** p) - 1) % number == 0.

    Args:
        number (int): The number to use to calculate the length of the cycle of
            repeating digits in 1/number.

    Returns:
        int: The length of the cycle of repeating digits.

    Raises:
        ValueError: number is <= 0, or a non-integer, or is not convertible to
        a float.
    """
    # Test that number is valid
    if not is_positive_integer(number):
        raise ValueError("input is not a positive intger")
    # Otherwise test the number
    d = 1
    while True:
        power = 10 ** d
        if (power - 1) % number == 0:
            return d
        d += 1
        if d == number:
            return 0

# Only runs if executed directly
if __name__ == '__main__':
    from euler.primes import prime_sieve
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=1000, help="find the longest cycle of 1/d for d less than or equal to MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    # Solution
    start_time = time()

    # We look only at primes. If n has a cycle of length m, then so do all
    # multiples of n. Therefore only primes have a chance at a new cycle
    # length.
    primes = prime_sieve(MAX)

    # We start at the end as the maximum cycle length is number - 1
    biggest_cycle = 0
    biggest_number = 0
    for i in reversed(primes):
        # Cycle is larger then remaining numbers, so their cycles must be
        # shorter
        if biggest_cycle >= i:
            break

        length = cycle_length(i)
        if length > biggest_cycle:
            biggest_cycle = length
            biggest_number = i

    end_time = time() - start_time
    print(biggest_number, 'with cycle length', biggest_cycle, 'in', end_time, 'secs')
