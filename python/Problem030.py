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
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

from euler.converter import int_to_tuple
from time import time


def problem_030(power=5):
    start_time = time()

    # Create a mapping of digits to power to speed the process (We could, of
    # course, use a list indexed by the digit, but this is the same speed and,
    # I feel, less clear than the explicit mapping a dictionary implies).
    powered_digits = {i: i**power for i in range(0, 10)}

    # For a fixed power, the largest number we'll need to sum is 9**power. Then
    # the largest number we can get from summing n digits like this is
    # n * (9**power). When the number of digits in this number is the same as N, we
    # have found the largest number we'll need to check, as all larger numbers
    # are too big to be generated.
    n = 1
    while True:
        stopping_point = n * (9 ** power)
        if len(int_to_tuple(stopping_point)) <= n:
            break
        n += 1

    # We do not consider sums of length 1 to be sums, so we must start with
    # numbers with at least 2 digits.
    total = 0
    for i in range(10, stopping_point + 1):
        number_tuple = int_to_tuple(i)
        sum_of_digits = sum((powered_digits[i] for i in number_tuple))
        if sum_of_digits == i:
            total += sum_of_digits

    end_time = time() - start_time
    print(total, 'in', end_time, 'secs')
    return total


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-p", action="store", type="int", dest="POW", default=5, help="find the sum of all numbers that are the sum of their digits to the POW power")

    (options, args) = parser.parse_args()

    # Constants
    POW = options.POW

    problem_030(POW)
