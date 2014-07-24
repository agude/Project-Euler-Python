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

    # Set up a dictionary mapping a number to the length of the chain for that number
    links_length = {1:1}

    max_count = 0
    max_number = None
    # Check every number
    for number in range(2, MAX):
        # Get chain length using the lookup table (it will exist if it has been computed before)
        count = 0
        try:
            count = links_length[number]
        # If we fail, compute the values until we make connection with the
        # table, and save all the values to speed up future computations
        except KeyError:
            modable_number = number
            stack = [number]

            while True:
                # Compute the new result
                if modable_number % 2:  # Odd
                    result = 3 * modable_number + 1
                else:  # Even
                    result = modable_number // 2

                # If the result is in the table, we're done, so we go back and
                # add all the numbers we have encountered so far
                if result in links_length:
                    base_length = links_length[result]
                    # We now go through the stack, with the last value being a
                    # distance 1 from the number we just found in the
                    # dictionary. We add the index value, as this tells us how
                    # far into the stack we are, and every level deeper is one
                    # more link in the chain we have to add to the total
                    # length.
                    for index, value in enumerate(reversed(stack)):
                        links_length[value] = base_length + 1 + index
                    break

                # Otherwise, keep generating numbers
                else:
                    stack.append(result)
                    modable_number = result

            # Now that we've updated the table, get the value
            count = links_length[number]

        # If the count length is a new max, save it
        if count > max_count:
            max_count = count
            max_number = number

    end_time = time() - start_time
    if MAX < 100:
        print(links_length)
    print(max_number, "with chain length", max_count, "in", end_time, "secs")
