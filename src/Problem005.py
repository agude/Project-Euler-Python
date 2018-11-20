#!/usr/bin/env python3

#  Copyright (C) 2011  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?
"""

from typing import List, Set
from euler.factorization import proper_factors


def problem_005(max_num: int = 20) -> int:
    from time import time

    # Solution
    start_time: float = time()

    # We can remove any numbers that are factors of other numbers in the list.
    # That is, if 2*N divides a number, then N does also.
    seen_divisors: Set[int] = set()
    final_divisors: List[int] = []
    for number in range(max_num, 1, -1):
        if number not in seen_divisors:
            final_divisors.append(number)

        current_factors: Set[int] = set(proper_factors(number))
        seen_divisors = seen_divisors.union(current_factors)

    # We know the number has to be divisible by the two largest numbers, so we
    # increment by the product of them.
    final_divisors.sort()
    largest: int = final_divisors.pop()
    second_largest: int = final_divisors.pop()
    increment: int = largest * second_largest

    # Find the smallest number divisible by all the coprime numbers
    test_number: int = 0
    while True:
        test_number += increment
        for j in final_divisors:
            if test_number % j:
                break
        else:  # Only if above doesn't break
            break

    total_time: float = time() - start_time
    print(test_number, 'in', total_time, 'secs')
    return test_number


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=20, help="answer must be divisible by 1, 2, 3 ... MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_005(MAX)
