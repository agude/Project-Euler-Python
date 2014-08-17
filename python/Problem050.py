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
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

# Only runs if executed directly
if __name__ == '__main__':

    from time import time
    from optparse import OptionParser
    from euler.primes import prime_sieve
    from sys import exit

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=1000000, help="find the prime below NUM that can be writen as the sum of the most consecutive primes")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    # Solution
    start_time = time()

    # Get the primes
    primes = prime_sieve(MAX)
    prime_set = set(primes)
    number_of_primes = len(primes)

    # We add the primes from smallest to largest until we get a number larger
    # than our maximum value. At that point, we know we never have to add more
    # than that many primes together, and so set a limit for our later loops.
    total = 0
    max_length = 0
    for i in range(len(primes)):
        total += primes[i]
        if total > MAX:
            break
        max_length += 1

    # We try all possible numbers of primes to sum, starting from the largest
    # number so that when we find one we know that we are done
    answer = 0
    number_summed = 0
    for number_to_sum in reversed(range(2, max_length + 1)):
        # The first one we find is the largest, so break
        if answer:
            break
        # Starting from the smallest prime, sum it and the next number_to_sum
        # primes. If this number is prime, we have a new best
        for start in range(0, number_of_primes - number_to_sum + 1):
            test_num = sum(primes[start:start + number_to_sum])
            # Since we work our way up the prime list from small to larger
            # primes, we know that as soon as the sum exceeds our max, all
            # further sums of this many digits will too.
            # break
            if test_num > MAX:
                break
            # As soon as we find one prime, we are done
            if test_num in prime_set:
                answer = test_num
                number_summed = number_to_sum
                break

    end_time = time() - start_time
    print(answer, "from summing", number_to_sum, "primes in", end_time, "secs")
