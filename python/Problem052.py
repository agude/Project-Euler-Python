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
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser
    from time import time
    from sys import exit

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NTH", default=6, help="")

    (options, args) = parser.parse_args()

    # Read in options
    NTH = options.NTH

    # Solution
    start_time = time()

    # Brute force numbers
    answer = 0
    while True:
        answer += 1
        starting_digits = str(answer)
        loop = True
        # Compute the multiples
        for multiple in range(2, NTH + 1):
            if not loop:
                break
            # Make sure we have the same digits
            test_number = str(answer * multiple)
            for digit in test_number:
                if digit not in starting_digits:
                    loop = False
                    break
        if loop:
            # We're done
            end_time = time() - start_time
            print(answer, 'in', end_time, 'secs')
            exit(0)
