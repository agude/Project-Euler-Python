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
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:

    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97

How many circular primes are there below one million?
"""

from euler.primes import prime_sieve, circular_primes
from optparse import OptionParser
from time import time


def problem_035(num=1000000):
    start_time = time()

    primes = set(prime_sieve(num - 1))
    final_primes = set([])
    for prime in primes:
        # Avoid double counting sets
        if prime in final_primes:
            continue
        # Otherwise try to get the circular primes, and if we get any add them
        # to our final list
        circulars = circular_primes(prime, prime_list=primes)
        if circulars:
            final_primes = final_primes.union(circulars)

    answer = len(final_primes)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n number"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="int", dest="NUM", default=1000000, help="find the number of circular primes below NUM.")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_035(NUM)
