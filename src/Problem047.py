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
The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 x 7
    15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2**2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""

from time import time
from euler.primes import prime_factors


def problem_047(num=4):
    start_time = time()

    # We brute force search to find the answer
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    count = num
    # The start number can't possibly be smaller than the product of the first
    # num primes, or else it fails our first test
    current_number = 1
    for i, prime in enumerate(primes):
        if i >= count:
            break
        current_number *= primes[i]
    print(current_number)
    previous_matches = 0
    start_number = None
    answer = None
    while True:
        factors = prime_factors(current_number)
        number_of_unique_factors = len(set(factors))
        # If the number has the right number of factors, increase by 1 the
        # number of consecutive numbers with this property seen. If it does
        # not, then reset the count.
        if number_of_unique_factors == num:
            previous_matches += 1
            if previous_matches == 1:
                start_number = current_number
        else:
            previous_matches = 0
            start_number = None

        # If we have as many numbers as we are looking for, end
        if previous_matches == num:
            answer = start_number
            break

        # Otherwise keep iterating
        current_number += 1

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=4, help="find the first set of NUM consequtive numbers with NUM distinct prime factors each")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_047(NUM)
