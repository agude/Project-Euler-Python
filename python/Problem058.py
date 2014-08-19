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
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.primes import is_prime
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="float", dest="NUM", default=0.1, help="find when the percent of primes first falls below NUM")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    # Solution
    start_time = time()

    # We can generate just the diagonals by noting that the corners are each
    # side_length - 1 from each other, and from the last corner of the previous
    # square. We continue to generate the diagonals and keep track of the ratio
    # until we reach the desired level.
    diagonals = [1]
    side_length = 1
    number_of_primes = 0
    answer = None

    while True:
        side_length += 2
        offset = side_length - 1
        last_end_point = diagonals[-1]

        # Generate the four numbers we need to add to the diagonal
        new_numbers = [last_end_point + (i * offset) for i in range(1, 5)]

        # Check for primes
        for number in new_numbers:
            if is_prime(number):
                number_of_primes += 1

        # Add the new numbers to the list and check the new ratio
        diagonals += new_numbers
        if number_of_primes / len(diagonals) <= NUM:
            answer = side_length
            break

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
