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
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from time import time


def problem_063(verbose=False):
    start_time = time()

    answer = 0
    power = 0
    # We first loop over powers, and then bases. When the length grows beyond
    # the power, all future bases of the power will also be too large, so we
    # break. When we fail to find a set that satisfy our criteria in the inner
    # loop, we are done with the problem.
    while True:
        old_answer = answer
        power += 1
        base = 0
        while True:
            base += 1
            result = base ** power
            length = len(str(result))
            if length == power:
                answer += 1
                if verbose:
                    print(result, '=', base, '**', power)
            elif length > power:
                break

        # If the inner loop failed to find any, than we have reached the end as
        # all future base ** power results will be too large to satisfy our
        # criteria.
        if old_answer == answer:
            break

    end_time = time() - start_time
    if verbose:
        print()
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose", action="store_true", dest="VERBOSE", default=False, help="print status messages to stdout [default False]")

    (options, args) = parser.parse_args()

    # Read in options
    VERBOSE = options.VERBOSE

    problem_063(VERBOSE)
