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
Consider the fraction, n/d, where n and d are positive integers. If n<d and
GCD(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for
d <= 1,000,000?
"""

from euler.totient import totient_sieve
from time import time


def problem_072(max_num=1000000):
    start_time = time()

    # The number of reduced fractions for a denominator d is simply the number
    # of coprime numbers less than d. This is, of course, Euler's Totient, so
    # we simply loop over denominators and calculate the totient.
    answer = 0
    totients = totient_sieve(max_num)
    # We subtract 1 because we don't want phi(1) = 1, since 1/1 is not a fully
    # reduced fraction.
    answer = sum(totients) - 1

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=1000000, help="find the number of unique reduced fractions with denominators from 2 to MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_072(MAX)
