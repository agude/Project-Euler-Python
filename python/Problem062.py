#!/usr/bin/env python3

#  Copyright (C) 2018  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104
(384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has
exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""


# Functions
def problem_062(permutations=5):
    from time import time
    from collections import defaultdict
    from euler.converter import sort_digits
    from itertools import count

    # Solution
    start_time = time()

    # The solution is pretty simple, just cube numbers, take the cube and sort
    # it so we have a unique representation of a set of permutations, and then
    # count how many cubes have the same representation.
    key_to_first = {}
    key_counter = defaultdict(int)
    final = None
    for i in count():
        cube = i ** 3
        key = sort_digits(cube)

        # If we have never seen this key before, save the number that generated
        # it, so we can find the solution after we have counted
        if key not in key_to_first:
            key_to_first[key] = i

        # If we have seen it, check if we have seen it five times
        if key in key_counter:
            seen_count = key_counter[key]
            if seen_count == permutations - 1:  # Plus now is the target number
                final = key_to_first[key]
                break

        key_counter[key] += 1

    end_time = time() - start_time
    print(final, 'in', end_time, 'secs')

    return final


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--permutations", action="store", type="int", dest="PERM", default=5, help="The number of permutations of the cube that are cubes.")

    (options, args) = parser.parse_args()

    # Constants
    PERM = options.PERM

    problem_062(PERM)
