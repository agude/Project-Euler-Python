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
n! means n * (n − 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the
digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.converter import int_to_tuple
    from math import factorial
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n NUM"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=100, help="find the sum of the digits of NUM!")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    # Solution
    start_time = time()

    factorial_number = factorial(NUM)
    answer = sum(int_to_tuple(factorial_number))

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
