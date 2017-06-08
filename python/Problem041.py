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
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from euler.pandigital import pandigitals
from euler.primes import is_prime
from time import time


def problem_041(nth=9):
    start_time = time()

    # Get all the pandigitals numbers (there are fewer pandigitals than primes)
    # and test them for primality
    pandigital_tuple = tuple(pandigitals(maximum_digits=nth))
    for test_number in reversed(pandigital_tuple):
        if is_prime(test_number):
            answer = test_number
            break

    end_time = time() - start_time

    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NTH", default=9, help="find the largest n-digit pandigital prime")

    (options, args) = parser.parse_args()

    # Read in options
    NTH = options.NTH

    problem_041(NTH)
