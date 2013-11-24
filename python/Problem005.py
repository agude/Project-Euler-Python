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
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?
"""

# Only runs if executed directly
if __name__ == '__main__':
    from time import time
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=20, help="answer must be divisible by 1, 2, 3 ... MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    # Solution
    start_time = time()

    # Find the set of coprime numbers in our set
    divs = [True] * MAX
    for i in range(len(divs)):
        numi = i + 1
        for j in range(len(divs)):
            if divs[j] and i > j:
                numj = j + 1
                if not numi % numj:
                    divs[j] = False

    nums = []
    for i in range(len(divs)):
        if divs[i]:
            nums.append(i + 1)

    a = nums.pop()
    b = nums.pop()

    # Find the smallest number divisible by all the coprime numbers
    i = 0
    while True:
        # We know the number has to be divisible by a and b, so we increment by
        # this number
        i += a * b
        for j in nums:
            if i % j:
                break
        else:  # Only if above doesn't break
            break

    total_time = time() - start_time
    print(i, 'in', total_time, 'secs')
