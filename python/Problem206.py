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
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit, but not necessarily the same.
"""

from euler.converter import iterable_to_int, int_to_tuple
from math import sqrt
from time import time


def problem_206():
    start_time = time()

    # We brute force a solution by trying all permutations, but with some
    # limiting simplifications:
    #
    # - Since our target number ends in 0 and the root is an integer, the root
    #   must also end in 0, but that means that our target number must end in
    #   00.
    # - After removing the 00, we have a 9, but only 3^2 and 7^2 end in 9, so
    #   we only need to check roots that end in [37]0.

    # We brute force check every root, but we can remove the ending 00, and
    # then we remove an extra digit and add the 3 or 7 by hand.
    MIN = iterable_to_int(int_to_tuple(int(sqrt(11213141516171819)))[:-1])
    MAX = iterable_to_int(int_to_tuple(int(sqrt(19293949596979899)))[:-1])
    for root in range(MIN, MAX):
        # We know the root must end in 30 or 70, so add on the 3 or 7
        for end_digit in (3, 7):
            new_root = root * 10 + end_digit
            result = new_root ** 2
            result_tuple = int_to_tuple(result)
            # Check that the 1,2,3... criterion holds
            for i in range(0, len(result_tuple), 2):
                # The 0th digit is 1, the 3rd digit is 2, etc.
                digit = (i / 2) + 1
                if result_tuple[i] != digit:
                    break
            # We know only one number satisfies the criteria, so when we find
            # it we terminate
            else:
                answer = new_root * 10
                end_time = time() - start_time
                print(answer, '** 2 =', answer**2, 'in', end_time, 'secs')
                return answer

# Only runs if executed directly
if __name__ == '__main__':

    problem_206()
