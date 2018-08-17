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
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from typing import Set


def problem_001(max_num: int = 1000) -> int:
    from time import time

    # Solution
    start_time = time()

    # Generate the sets of numbers
    threes: Set[int] = set(range(3, max_num, 3))
    fives: Set[int] = set(range(5, max_num, 5))
    all_nums: Set[int] = fives.union(threes)
    total: int = sum(all_nums)

    end_time: float = time() - start_time
    print(total, 'in', end_time, 'secs')
    return total


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=1000, help="find the sum of the multiples of 3 or 5 below MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_001(MAX)
