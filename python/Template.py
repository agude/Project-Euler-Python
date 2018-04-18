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
"""


# Functions
def problem_001(max_num=1000):
    from time import time

    # Solution
    start_time = time()

    # Generate the sets of numbers

    # SOLUTION
    total = 1

    end_time = time() - start_time
    print(total, 'in', end_time, 'secs')

    return total


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--num", action="store", type="int", dest="num", default=0, help="")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_001(MAX)
