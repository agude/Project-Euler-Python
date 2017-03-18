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
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

def problem_015(max_num=20):
    from euler.combinatorics import n_choose_k
    from time import time

    # Solution
    start_time = time()

    # We notice that we can encode a path as a binary number, where 1 means
    # "right" and 0 means "down". Then paths must be of length 2n, and there
    # must be n 1s and n 0s. Then to specify a path we just need to specify the
    # location of the 1s. The number of ways we can do this is 2n choose n.

    answer = n_choose_k(2 * max_num, max_num)
    end_time = time() - start_time
    print(answer, "in", end_time, "secs")
    return answer


if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=20, help="find the number of paths in an n*n graph")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_015(MAX)
