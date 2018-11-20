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
An irrational decimal fraction is created by concatenating the positive
integers:

    0.12345678910 >1< 112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

    d_1 *  d_10 *  d_100 * d_1000 *  d_10000 * d_100000 * d_1000000
"""

from time import time


def problem_040():
    start_time = time()

    # Generate the number as a string for easy slicing
    digits_list = ["0."] + [str(i) for i in range(1, 185186)]
    number = ''.join(digits_list)

    # Multiply the requested digits
    answer = 1
    for position in (1, 10, 100, 1000, 10000, 100000, 1000000):
        answer *= int(number[position + 1])

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    problem_040()
