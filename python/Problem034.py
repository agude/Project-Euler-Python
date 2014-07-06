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
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from time import time
    from math import factorial
    from euler.converter import int_to_tuple

    # Solution
    start_time = time()

    # We tried making a dictionary mapping digits to their factorial to speed
    # up the calculation, but it turns out the math.factorial uses a lookup
    # table for 0-20, so this method is no faster.
    #
    # factorials = {i: factorial(i) for i in range(10)}

    # The upper bounds is from Wikipedia:
    # http://en.wikipedia.org/wiki/Factorion
    #
    # If n is a natural number of d digits that is a factorion, then
    # 10 ** (d - 1) <= n <= 9! * d. This fails to hold for d >= 8 thus n has at
    # most 7 digits, and the first upper bound is 9,999,999. But the maximum
    # sum of factorials of digits for a 7 digit number is 9!*7 = 2,540,160
    # establishing the second upper bound. Going further, 9!6 is 2,177,280, and
    # the only 7 digit number not larger than 2,540,160 containing six 9's is
    # 1,999,999, which is not a factorion by inspection. The next highest sum
    # would be given by 1,999,998, yielding a third upper bound of 1,854,721.
    #
    answer = 0
    for number in range(3, 1854722):
        tuple_number = int_to_tuple(number)
        digit_sum = sum((factorial(digit) for digit in tuple_number))
        if digit_sum == number:
            print("Found a factorion:", number)
            answer += number

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
