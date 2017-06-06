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
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from euler.factorization import proper_factors
from time import time


def problem_021(num=10000):
    # Solution
    start_time = time()

    # We run through all numbers and test to see if they are amicable. If they
    # are, we add them to a set and use this to reject duplicates.
    pairs = set([])
    for number in range(1, num):
        if number not in pairs:
            number_to_check = sum(proper_factors(number))
            # We have already checked all numbers smaller than our number. This
            # also correctly rejects perfect numbers (numbers where d(n) = n).
            if number_to_check > number:
                is_amicable = sum(proper_factors(number_to_check)) == number
                if is_amicable:
                    pairs.add(number)
                    pairs.add(number_to_check)

    # Finally sum our amicable numbers to get the answer
    answer = sum(pairs)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n number"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="int", dest="NUM", default=10000, help="find the sum of all amicable numbers under NUM")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_021(NUM)
