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
The following iterative sequence is defined for the set of positive integers:

    n --> n/2 (n is even)
    n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

if __name__ == '__main__':
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "-m", "--max", action="store", type="int", dest="MAX", default=1000000, help="find the number that produces the longest chain searching from 0 to MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    # Solution
    start_time = time()

    # Set up a dictionary mapping a number to the next number for all numbers
    # up to MAX so that we only have to compute the numbers once ever
    links = {number: (number // 2) for number in range(2, MAX, 2)}
    links.update({number: (3 * number + 1) for number in range(3, MAX, 2)})

    # Using our lookup table, we follow our way through it until we hit 1. If
    # we hit a number we don't yet know, we add it.
    max_count = 0
    max_number = None
    # Check every number
    for number in range(2, MAX):
        modable_number = number
        # Compute the chain length using the lookup table
        count = 0
        while modable_number != 1:
            try:
                modable_number = links[modable_number]
            # If we fail, compute the value and save it in the table
            except KeyError:
                # We need to add the number and its result to our dictionary
                if modable_number % 2:  # Odd
                    result = 3 * modable_number + 1
                else:  # Even
                    result = modable_number // 2
                links[modable_number] = result
                modable_number = result
            # Always increment the chain length, exception or not
            finally:
                count += 1

        # If the count length is a new max, save it
        if count > max_count:
            max_count = count
            max_number = number

    end_time = time() - start_time
    print(max_number, "with chain length", max_count, "in", end_time, "secs")
