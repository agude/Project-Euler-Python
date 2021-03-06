#!/usr/bin/python3
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

""" The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144

The 12th term, F_12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

from time import time
from euler.fibonacci import fibonacci_generator


def problem_025(num=1000):
    start_time = time()

    term = -1
    for number in fibonacci_generator():
        term += 1
        if len(str(number)) >= num:
            break

    end_time = time() - start_time
    print(term, 'in', end_time, 'secs')
    return term


if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=1000, help="find the first Fibonacci number with NUM digits")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_025(NUM)
