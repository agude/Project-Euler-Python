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
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from time import time

from euler.palindromic import is_palindromic


def problem_004(min_num=100, max_num=999):
    # Solution
    start_time = time()

    largest_seen = 0
    for a in range(max_num, min_num, -1):
        for b in range(a, min_num - 1, -1):
            newest_number = a * b
            if is_palindromic(newest_number):
                break
            elif newest_number < largest_seen:
                newest_number = -1
                break
            else:
                newest_number = -1
        largest_seen = max(largest_seen, newest_number)

    total_time = time() - start_time
    print(largest_seen, 'in', total_time, 'secs')
    return largest_seen


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -m MAX -n MIN"
    parser = OptionParser(usage=usage)
    parser.add_option("-m", action="store", type="int", dest="MAX", default=999, help="find a palindromic number by multiplying numbers <= MAX")
    parser.add_option("-n", action="store", type="int", dest="MIN", default=100, help="find a palindromic number by multiplying numbers >= MIN")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX
    MIN = options.MIN

    problem_004(MIN, MAX)
