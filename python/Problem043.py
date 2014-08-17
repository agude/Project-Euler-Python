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
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2 d3 d4  = 406 is divisible by 2
    d3 d4 d5  = 063 is divisible by 3
    d4 d5 d6  = 635 is divisible by 5
    d5 d6 d7  = 357 is divisible by 7
    d6 d7 d8  = 572 is divisible by 11
    d7 d8 d9  = 728 is divisible by 13
    d8 d9 d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from time import time
    from euler.pandigital import pandigitals
    from euler.converter import iterable_to_int, int_to_tuple

    # Solution
    start_time = time()

    # Hardcoded first digit, last digit + 1, and the prime number to compare to
    slices = (
        (1, 4, 2),
        (2, 5, 3),
        (3, 6, 5),
        (4, 7, 7),
        (5, 8, 11),
        (6, 9, 13),
        (7, 10, 17),
    )

    # We search all the 10 digit pandigital numbers
    answer = 0
    for pandigital in pandigitals(10, 10, True):
        pandigital_tuple = int_to_tuple(pandigital)
        # We use our hard-coded values to slice the digits number and to get
        # our divisor
        for start, stop, divisor in slices:
            test_number = iterable_to_int(pandigital_tuple[start:stop])
            if test_number % divisor:
                break
        else:
            print("Adding:", pandigital)
            answer += pandigital

    end_time = time() - start_time
    print(answer, "in", end_time, "secs")
