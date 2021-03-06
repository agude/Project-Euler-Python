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
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def problem_010(max_num=2000000):
    from time import time
    from euler.primes import prime_sieve

    # Solution
    start_time = time()

    primes = prime_sieve(max_num - 1)

    result = primes.sum()
    total_time = time() - start_time
    print(result, 'in', total_time, 'secs')
    return result


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "-m", "--NUM", action="store", type="int", dest="MAX", default=2000000, help="sum all primes below MAX")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_010(MAX)
