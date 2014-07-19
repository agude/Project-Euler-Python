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
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

# Only runs if executed directly
if __name__ == '__main__':
    from time import time
    from optparse import OptionParser
    from euler.palindromic import is_palindromic, is_binary_palindromic

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n NUM"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=1000000, help="sum all numbers less than NUM that are palindromic in base 10 and base 2")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    # Solution
    start_time = time()

    # We search all numbers and check them
    answer_numbers = []
    for i in range(1, NUM):
        if is_palindromic(i) and is_binary_palindromic(i):
            answer_numbers.append(i)

    answer = sum(answer_numbers)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
