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
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

from bisect import insort
from euler.factorization import proper_factors
from time import time


def problem_023():
    # All numbers > 28123 are the sum of two abundant
    LARGEST_NUMBER = 28123

    # Solution
    start_time = time()

    # Generate abundant numbers. We store a set for quick checking, and a
    # sorted list in order to loop through them when checking if the number is
    # a sum.
    abundant = set([])
    sorted_abundant = []
    for i in range(1, LARGEST_NUMBER + 2):
        if sum(proper_factors(i)) > i:
            abundant.add(i)
            insort(sorted_abundant, i)

    # Check numbers
    answer = 0
    for i in range(1, LARGEST_NUMBER + 1):
        for j in sorted_abundant:
            # If we're here, it passes our criteria and we add it
            if j >= i:
                answer += i
                break
            # Sum of two abundant, reject
            if i - j in abundant:
                break

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    problem_023()
