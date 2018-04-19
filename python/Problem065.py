#!/usr/bin/env python3

#  Copyright (C) 2018  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104
(384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has
exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""


from itertools import count
from euler.countable import is_integer


# Functions

def euler_an(n):
    # The first one doesn't follow the pattern
    if n == 1:
        return 1

    # The rest of the pattern is 2, 1, 1, 4, 1, 1, 6, 1, 1 ...
    # We start by adjusting so that the first two is the 0th index
    new_n = n - 2

    mod = new_n / 3

    if not is_integer(mod):
        return 1

    return 2 + (2 * int(mod))


def problem_065(convergent=100):
    from time import time
    from euler.fractions import ContinuedFraction
    from euler.converter import sum_digits

    # Solution
    start_time = time()

    # The solution is pretty simple, just cube numbers, take the cube and sort
    # it so we have a unique representation of a set of permutations, and then
    # count how many cubes have the same representation.
    cf = ContinuedFraction(2, euler_an)

    numerator = cf.nth_convergent_numerator(convergent-1)
    print(numerator)

    final = sum_digits(numerator)

    end_time = time() - start_time
    print(final, 'in', end_time, 'secs')

    return final


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--convergent", action="store", type="int", dest="CONV", default=100, help="The sum of the CONV convergent's numerator.")

    (options, args) = parser.parse_args()

    # Constants
    CONV = options.CONV

    problem_065(CONV)
