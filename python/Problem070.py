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
Euler's Totient function, phi(n), is used to determine the number of positive
numbers less than or equal to n which are relatively prime to n. For example,
as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine,
phi(9)=6.  The number 1 is considered to be relatively prime to every positive
number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10**7, for which phi(n) is a permutation of n and
the ratio n/phi(n) produces a minimum.
"""

from euler.converter import int_to_tuple
from euler.totient import totient_sieve
from time import time


def problem_070(max_num=int(10**7)):
    start_time = time()

    # Calculate all the totients
    totients = totient_sieve(max_num)

    # Loop through all of them and find all pairs such that phi is a permutation
    # of the digits of n. For these, save the one with the lowest ratio
    # n / phi.
    minimum = float("inf")
    min_n = 0
    for n in range(2, len(totients)):
        phi = totients[n]
        # Check for pairs where phi is a permutation of n's digits
        if sorted(int_to_tuple(n)) == sorted(int_to_tuple(phi)):
            ratio = n / phi
            if ratio < minimum:
                minimum = ratio
                min_n = n

    end_time = time() - start_time
    print(min_n, 'in', end_time, 'secs')
    return min_n


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=int(10**7), help="find the lowest n / phi where phi and n are permutations of each other from 2 to MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_070(MAX)
