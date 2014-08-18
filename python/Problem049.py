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
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
    1) each of the three terms are prime
    2) each of the 4-digit numbers are permutations of one another

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.converter import int_to_tuple, iterable_to_int
    from euler.primes import prime_sieve
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=4, help="check NUM-digit primes for a sequence")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM
    MIN = 10 ** (NUM - 1)
    MAX = (10 ** NUM) - 1

    # Solution
    start_time = time()

    # Make a set of primes from MIN to MAX
    primes = prime_sieve(MAX)
    primes = primes[primes >= MIN]
    # Use a set for faster lookup
    primes_set = set(primes)

    # Brute force search by looking for primes of the form k = j + (j - i). For
    # each set of primes i, j, k, see if their digits are a permutation of
    # each other.
    concatenated_prime = ()
    for i in range(len(primes) - 1):
        first_prime = primes[i]
        first_permuation = sorted(int_to_tuple(first_prime))
        for j in range(i + 1, len(primes)):
            second_prime = primes[j]
            second_permuation = sorted(int_to_tuple(second_prime))
            diff = second_prime - first_prime
            third_prime = second_prime + diff
            # As soon as the sum is greater than MAX, all future values will be
            # as well
            if third_prime > MAX:
                break
            if third_prime in primes_set:
                # Now check permutations
                third_permuation = sorted(int_to_tuple(third_prime))
                if third_permuation == second_permuation == first_permuation:
                    print(first_prime, second_prime, third_prime)
                    # Concatenate and save the result; the last of these will
                    # be the answer we want
                    concatenated_prime = (
                        first_permuation
                        + second_permuation
                        + third_permuation
                    )

    # Form the answer from the tuple of concatenated primes
    answer = None
    if concatenated_prime:
        answer = iterable_to_int(concatenated_prime)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
