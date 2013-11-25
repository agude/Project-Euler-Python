#!/usr/bin/env python3

#  Copyright (C) 2011  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

# Only runs if executed directly
if __name__ == '__main__':
    from library import PrimeSieve
    from math import log
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n NUM"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=10001, help="find the NUM'th prime")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    # Solution
    start_time = time()

    # We need an upper bound on the prime to use the fast sieve:
    # P_n <= n * log(n) + n log(log(n)) for n >= 6
    if NUM >= 6:
        MAX = NUM * log(NUM) + NUM * log(log(NUM))
        primes = PrimeSieve(MAX)
    elif NUM > 0:
        primes = [2, 3, 5, 7, 11]
    else:
        primes = None

    total_time = time() - start_time
    if primes is not None:
        print(primes[NUM - 1], 'in', total_time, 'secs')
    else:
        print(primes, 'in', total_time, 'secs')
