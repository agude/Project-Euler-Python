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
The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.

Find the last ten digits of the series:
    1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000)
"""

# Only runs if executed directly
if __name__ == '__main__':
    from time import time
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n number"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="int", dest="NUM", default=1000, help="find the last ten digits of the sum NUM**NUM")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    # Solution
    start_time = time()

    # No tricks, we just compute the number and grab the last 10 digits
    sum_of_squares = sum((i ** i for i in range(1, NUM + 1)))

    number_string = str(sum_of_squares)
    answer = int(number_string[-10:])

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
