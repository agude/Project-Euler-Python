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
The square root of 2 can be written as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

The infinite continued fraction can be written, sqrt(2) = [1;(2)], (2)
indicates that 2 repeats ad infinitum. In a similar way, sqrt(23) =
[4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for sqrt(2).

The first ten convergents of sqrt(2) are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""


from euler.countable import is_integer


# Functions
def euler_an(n):
    """Return the a_{n} coefficients for the continued fraction of e.

    Args:
        n (int): The number of the coefficient.

    Returns:
        int: The nth coefficient.
    """
    # The first one doesn't follow the pattern
    if n == 1:
        return 1

    # The rest of the pattern is 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...
    # We start by adjusting so that the 2 is the 0th index
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
    cf = ContinuedFraction(a0=2, an=euler_an)

    # We index from 0 (to follow the a_{n} convention), but Project Euler
    # refers to the "100th" convergent, which is 99 for us. So we subtract 1.
    numerator = cf.nth_convergent_numerator(convergent-1)

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
    parser.add_option("-n", "--convergent", action="store", type="int", dest="CONV", default=100, help="The sum of the CONV th convergent's numerator.")

    (options, args) = parser.parse_args()

    # Constants
    CONV = options.CONV

    problem_065(CONV)
