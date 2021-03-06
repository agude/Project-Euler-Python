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
A googol (10**100) is a massive number: one followed by one-hundred zeros;
100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the
maximum digital sum?
"""

from collections import namedtuple
from time import time

from euler.converter import int_to_tuple


SumAndBaseAndPower = namedtuple("SumAndBaseAndPower", ["sum", "base", "power"])


def problem_056(max_base=100, max_power=100):
    start_time = time()

    # We simply brute force the solution
    biggest_seen = SumAndBaseAndPower(0, 0, 0)
    for base in range(1, max_base + 1):
        for power in range(1, max_power + 1):
            new_sum = sum(int_to_tuple(base ** power))

            newest_seen = SumAndBaseAndPower(new_sum, base, power)
            biggest_seen = max(biggest_seen, newest_seen)

    end_time = time() - start_time
    from_str = "from {base}**{power}".format(base=biggest_seen.base, power=biggest_seen.power)
    print(biggest_seen.sum, from_str, 'in', end_time, 'secs')
    return biggest_seen.sum


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-a", action="store", type="int", dest="MAX_BASE", default=100, help="For a**b, check a from 1 to MAX_BASE [default 100]")
    parser.add_option("-b", action="store", type="int", dest="MAX_POWER", default=100, help="For a**b, check b from 1 to MAX_BASE [default 100]")

    (options, args) = parser.parse_args()

    # Constants
    MAX_BASE = options.MAX_BASE
    MAX_POWER = options.MAX_POWER

    problem_056(MAX_BASE, MAX_POWER)
