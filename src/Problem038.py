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
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n  1?
"""

from euler.pandigital import is_pandigital
from euler.primes import is_prime
from time import time


def problem_038():
    start_time = time()

    # The fixed_number must start with 9 since we are given that the number is
    # larger than 918273645. Then we have the following cases for the length of
    # the fixed_number:
    #
    #     - 1 Digit: Already tried in the example
    #     - 2 Digit: Multiplication leads to an output with 2, 5, 8, 11 digits
    #     - 3 Digit: Multiplication leads to an output with 3, 7, 11 digits
    #     - 4 Digit: Multiplication leads to an output with 4, 9 digits
    #     - 5 Digit: Multiplication leads to an output with 5, 11 digits
    #
    # Therefore only the 4 digit case is possible as only it yields a case with
    # 9 digits. Further we now know that we have to multiple only by (1, 2).
    # The starting number must be greater than 9182 or the output will be
    # smaller than out proven largest from the example. The maximum is 9876,
    # because otherwise it won't be pandigital.
    answer = None
    for fixed_number in range(9876, 9182, -1):
        string_number = str(fixed_number) + str(fixed_number * 2)
        if is_pandigital(int(string_number)):
            answer = int(string_number)
            break

    end_time = time() - start_time

    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    problem_038()
