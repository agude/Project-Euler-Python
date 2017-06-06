#!/usr/bin/env python3

#  Copyright (C) 2011  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

from euler.spiral import Spiral
from time import time


def problem_028(num=1001):
    start_time = time()

    sp = Spiral(num)
    sp_sum = sp.sum

    end_time = time() - start_time
    print(sp_sum, 'in', end_time, 'secs')
    return sp_sum


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n number"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="int", dest="NUM", default=1001, help="find the sum of the diagonals of a NUM x NUM spiral")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_028(NUM)
