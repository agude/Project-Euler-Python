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

""" Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed
four million.
"""

def problem_002(max_num: int = 4000000) -> int:
    from time import time
    from euler.fibonacci import fibonacci_generator

    # Solution
    start_time: float = time()

    # We compute all the Fibonacci numbers and check them
    total: int = 0
    for number in fibonacci_generator():
        # Break when we hit the limit
        if number > max_num:
            break
        # Add only if even
        elif not number % 2:
            total += number

    end_time: float = time() - start_time
    print(total, 'in', end_time, 'secs')
    return total


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=4000000, help="find the sum of the even numbers in the Fibonacci sequence below MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_002(MAX)
