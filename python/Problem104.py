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
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.

It turns out that F_541, which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F_2749, which contains 575
digits, is the first Fibonacci number for which the first nine digits are 1-9
pandigital.

Given that F_k is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.pandigital import is_pandigital
    from euler.fibonacci import fibonacci_generator, fibonacci_binet
    from euler.converter import int_to_tuple, iterable_to_int
    from time import time

    # Solution
    start_time = time()

    # We make use of the fact that we only need to check the last 9 digits,
    # which means we can mod the Fibonacci numbers to pick out just those
    # digits without disrupting the sequence. Once we find a number where the
    # last 9 are pandigital, we check the first 9 using Binet's formula to
    # generate the Fibonacci number. Although this has inaccuracies due to the
    # limitation of doubles, it does not effect the left most digits.
    count = -1
    for number in fibonacci_generator(mod=1000000000):
        count += 1
        # We have to avoid 12, which otherwise passes our requirements because
        # slicing grabs as many characters as are available.
        if len(str(number)) < 3:
            continue
        # If the first 9 digits are pan
        if is_pandigital(number):
            full_fibonacci = fibonacci_binet(count)
            front_tuple = int_to_tuple(full_fibonacci)[:9]
            front_int = iterable_to_int(front_tuple)
            if is_pandigital(front_int):
                answer = count
                break
    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
