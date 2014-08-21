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
Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 +
904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are
reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.converter import iterable_to_int, int_to_tuple
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=1000000000, help="find the number of reversible numbers below MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    # Solution
    start_time = time()

    # Loop over all the numbers and test. We note that we only have to loop
    # over half the numbers because in order for every digit of a number to be
    # odd, the number itself must be odd. The only way to get an odd number is
    # to add an odd and an even number. Hence we loop only over odd numbers.
    reversibles = set([])
    for number in range(1, MAX, 2):
        reversed_tuple = int_to_tuple(number)[::-1]

        # Numbers that start with 0 are not allowed
        if not reversed_tuple[0]:
            continue

        # Compute the resulting number
        reversed_int = iterable_to_int(reversed_tuple)
        result = number + reversed_int
        result_tuple = int_to_tuple(result)

        # Check if the resulting digits are all odd
        for digit in result_tuple:
            if not digit % 2:
                break
        # If they are, add both numbers
        else:
            reversibles.add(number)
            reversibles.add(reversed_int)

    answer = len(reversibles)
    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
