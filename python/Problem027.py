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
Euler published the remarkable quadratic formula:

    n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40**2 + 40 + 41 = 40*(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n**2 - 79*n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The product of
the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.primes import is_prime
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-a", "--a_max", action="store", type="int", dest="AMAX", default=1000, help="enforce |a| < AMAX in n**2 + a*n + b")
    parser.add_option("-b", "--b_max", action="store", type="int", dest="BMAX", default=1000, help="enforce |b| < BMAX in n**2 + a*n + b")

    (options, args) = parser.parse_args()

    # Constants
    A_MAX = options.AMAX
    B_MAX = options.BMAX

    # Solution
    start_time = time()

    best = 0
    best_a = 0
    best_b = 0
    for a in range(-A_MAX, A_MAX + 1):
        for b in range(-B_MAX, B_MAX + 1):
            consecutive_primes = 0
            n = 0
            while is_prime(n*n + a*n + b):
                consecutive_primes += 1
                n += 1
            if consecutive_primes > best:
                best_a = a
                best_b = b
                best = consecutive_primes

    end_time = time() - start_time
    print(best, 'in', end_time, 'secs')