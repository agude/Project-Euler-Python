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
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over
half of the numbers below one-thousand (525) are bouncy. In fact, the least
number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly
99%.
"""

from euler.bouncy import is_bouncy
from time import time


def problem_112(ratio=0.99):
    start_time = time()

    # We do a simple brute force calculation over all numbers until we reach
    # the desired ratio. We start at 100, because no numbers under 100 are
    # bouncy.
    total = 99
    bouncy = 0
    while bouncy / total < ratio:
        total += 1
        if is_bouncy(total):
            bouncy += 1

    answer = total

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="float", dest="RATIO", default=0.99, help="Find the point at which the ratio of bouncy numbers / all tested numbers is equal to RATIO")

    (options, args) = parser.parse_args()

    # Constants
    RATIO = options.RATIO

    problem_112(RATIO)
