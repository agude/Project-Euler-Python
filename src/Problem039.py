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
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

from collections import namedtuple
from math import sqrt
from time import time

from euler.countable import is_integer


CombosAndParameters = namedtuple("CombosAndParameters", ["combos", "parameters"])


def problem_039(max_num=1000):
    start_time = time()

    # We note that are three cases:
    #  a even, b even -> c even -> p even
    #  a odd,  b odd  -> c even -> p even
    #  a even, b odd  -> c odd  -> p even
    #
    # So we need only check even parameters
    #
    # We further note that the triangle inequality holds:
    # a + b > c --> a + b + c > 2c --> p > 2c --> p/2 > c
    # c > a or b, hence p / 2 > c or a or b, so a and be need only run up
    # to p/2

    best_seen = CombosAndParameters(0, 0)
    # Remember we need only check even values
    for parameter in range(12, max_num+1, 2):  # 12 is smallest perimeter
        half_parameter = parameter // 2
        combos = 0
        # a, b, and c are constrained to be less than half of the parameter
        for a in range(1, half_parameter):
            # b + a can't be larger than parameter, and b can't be larger than
            # half the parameter, so the limit on b is the minimum of these two
            b_max = min(parameter - a, half_parameter)
            for b in range(a, b_max):
                c = sqrt(a * a + b * b)
                # Checking a + b + c == parameter is faster than the integer
                # check, so we put it first
                if a + b + c == parameter and is_integer(c):
                    combos += 1
        # Save the best
        newest_seen = CombosAndParameters(combos, parameter)
        best_seen = max(best_seen, newest_seen)

    end_time = time() - start_time
    print(best_seen.parameter, 'in', end_time, 'secs')
    return best_seen.parameter


if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=1000, help="find the perimeter that maximizes number of right triangles up to MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_039(MAX)
