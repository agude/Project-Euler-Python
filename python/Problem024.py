#!/usr/bin/env python3

#  Copyright (C) 2013  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

# Only runs if executed directly
if __name__ == '__main__':
    from math import factorial, floor
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS] digits"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NTH", default=1000000, help="find the Nth number in the permutations")

    (options, args) = parser.parse_args()

    # Set up input list of digits
    if not args:
        digits = [int(i) for i in range(0, 10)]
    else:
        digits = [int(i) for i in args]
    digits.sort()

    # Solution
    start_time = time()

    number = ""
    target_num = options.NTH - 1  # -1 because the list is zero indexed

    # We figure out the Nth number by combinatorics. We know that the first
    # (N-1)!  numbers will start with 0, and then the next set of (N-1)! will
    # start with 1, and so on. This allows us to fix the first digit (that is,
    # the digit to the far left). We repeat this process for all remaining
    # numbers until we reach our goal.
    while digits:
        # Number of digits left in our list
        digits_len = len(digits)
        # The size of the (N-1)! groups
        step_size = factorial(digits_len - 1)
        # The location in the sorted list of the digit to append from the right
        digit_place = floor(target_num / step_size)
        target_num -= digit_place * step_size
        digit = digits.pop(digit_place)
        number += str(digit)

    end_time = time() - start_time

    print(number, 'in', end_time, 'secs')
