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
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""


# Functions
def problem_057(stop_after=1000):
    from time import time
    from euler.fractions import continued_fraction_numerator, continued_fraction_denominator
    from euler.converter import int_to_tuple

    # Solution
    start_time = time()

    total = 0

    a0 = 1
    ai = lambda x: 2

    for i in range(0, stop_after+1):
        num = continued_fraction_numerator(i, a0, ai)
        den = continued_fraction_denominator(i, a0, ai)
        if len(int_to_tuple(num)) > len(int_to_tuple(den)):
            total += 1

    end_time = time() - start_time
    print(total, 'in', end_time, 'secs')

    return total


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--nth", action="store", type="int", dest="NTH", default=1000, help="Stop after computing the NTH convergent of sqrt(2)")

    (options, args) = parser.parse_args()

    # Constants
    NTH = options.NTH

    problem_057(NTH)
