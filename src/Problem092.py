#!/usr/bin/env python3

#  Copyright (C) 2017  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

from euler.digits import square_and_add
from time import time


def problem_092(max_num=10000000):
    start_time = time()

    # Memoize numbers that lead to 1 or 89 chains
    eightynines = set([4, 16, 20, 37, 42, 58, 85, 89, 145])
    ones = set([1, 10, 13, 32, 44])

    for i in range(2, max_num):
        # If we have already seen a number, then we know the answer
        if i in ones or i in eightynines:
            continue

        # Otherwise check until we loop, or hit something in memo
        seen = set([i])
        while True:
            i = square_and_add(i)
            seen.add(i)
            # We have hit a loop, mark all False
            if i == 1 or i in ones:
                ones.update(seen)
                break
            # We have hit 89 or a number we know leads there, mark all True
            if i == 89 or i in eightynines:
                eightynines.update(seen)
                break

    # Count the integers that belong to chains that end up in 89
    answer = len(eightynines)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n number"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="int", dest="NUM", default=10000000, help="find the sum of the diagonals of a NUM x NUM spiral")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM
    problem_092(NUM)
