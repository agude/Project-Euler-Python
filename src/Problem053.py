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
There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCk = n! / (k!(n-k)!), where k <= n, n! = n*(n-1)*...*3*2*1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 <= n <= 100, are
greater than one-million?
"""

from math import factorial
from euler.combinatorics import n_choose_k
from time import time


def problem_053(nth=100, max_val=1000000):
    start_time = time()

    # Check only the first half of the binomial coefficients, because they are
    # symmetric with regards to k, n-k.
    answer = 0
    for n in range(0, nth + 1):
        half_way = n // 2
        for k in range(0, half_way + 1):
            nck = n_choose_k(n, k)
            if nck > max_val:
                # If n and k are even, then that value only appears once,
                # otherwise the coefficients are symmetric so it appears twice.
                if k == half_way and not n % 2:
                    answer += 1
                else:
                    answer += 2

    # We're done
    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NTH", default=100, help="Check nCr from 1 to Nth [default 100]")
    parser.add_option("-m", action="store", type="int", dest="MAX", default=1000000, help="Find the number of nCr values greater than MAX [default  1000000]")

    (options, args) = parser.parse_args()

    # Read in options
    NTH = options.NTH
    MAX = options.MAX

    problem_053(NTH, MAX)
