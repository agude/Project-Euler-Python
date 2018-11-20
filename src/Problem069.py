#!/usr/bin/env python3

#  Copyright (C) 2010  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
Euler's Totient function, phi(n) [sometimes called the phi function], is used
to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, phi(9)=6.

n   Relatively Prime    phi(n)    n/phi(n)
2   1                   1         2
3   1,2                 2         1.5
4   1,3                 2         2
5   1,2,3,4             4         1.25
6   1,5                 2         3
7   1,2,3,4,5,6         6         1.1666...
8   1,3,5,7             4         2
9   1,2,4,5,7,8         6         1.5
10  1,3,7,9             4         2.5

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""

from time import time
from euler.primes import primes


def problem_069(max_num=1000000):
    start_time = time()

    # The totient function is equal to the product:
    #
    #     phi(n) = n * Product(p/(1-p))
    #
    # Where the product is over p, the unique primes dividing n. Therefore:
    #
    #     n / phi(n) = Product(p/(1-p))
    #
    # This  is maximal if n is the product of the first k prime numbers.

    # We construct n by multiplying the primes until we get a number larger
    # than the max.
    answer = 0
    running_product = 1
    for prime in primes():
        running_product *= prime
        if running_product > max_num:
            break
        answer = running_product

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n number -b"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--number", action="store", type="int", dest="NUM", default=1000000, help="find the max of n/phi(n) for 0 < n < NUM+1")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_069(NUM)
