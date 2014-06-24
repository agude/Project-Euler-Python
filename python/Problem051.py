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
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.primes import prime_sieve
    from euler.converter import iterable_to_int, int_to_tuple
    from itertools import combinations
    from time import time
    from copy import deepcopy
    from sys import exit

    # Solution
    start_time = time()

    # We loop over all primes and try all possible permutations of digit
    # replacement until we find one with 8 primes.

    # Loop over primes. We use the sieve and turn the result into a set so that
    # we can test primality very quickly, as we have to do this hundreds of
    # times per loop iteration. We grow the sieve as it is exhausted, such that
    # it always contains all of the possible numbers we'll need to check (that
    # is, for a test number with n digits, it always contains all the primes up
    # to the number containing n digits, all equal to 9).
    sieve_end = 99999
    last_prime = 56773
    while True:
        primes = prime_sieve(sieve_end)
        prime_set = frozenset(primes)
        for base_prime in primes:
            # We know the largest prime of the set with 7 primes is 56773, so start
            # there as any with 8 would have been found already if they were smaller.
            if base_prime < last_prime:
                continue
            # We convert the number to a tuple so that it is easier to
            # manipulate the digits.
            base_tuple = int_to_tuple(base_prime)
            digits = range(len(base_tuple))
            # Numbers are not allowed to lose (or gain) digits under the
            # substitution; we insure this by making sure the resulting numbers
            # are between min and max.
            min_num = iterable_to_int(len(base_tuple) * [1])
            max_num = iterable_to_int(len(base_tuple) * [9])
            # Compute the possible digit substitutions; we use combinations to
            # as to avoid duplicates that come from assuming position matters
            # (that is for our case [1, 2] is the same as [2, 1], so we don't
            # need or want the latter).
            for number_to_replace in range(1, len(base_tuple)):
                for digits_to_replace in combinations(digits, number_to_replace):
                    new_primes = []
                    for new_digit in range(0, 10):
                        new_list = list(deepcopy(base_tuple))
                        for replace_digit in digits_to_replace:
                            new_list[replace_digit] = new_digit
                        new_number = iterable_to_int(new_list)
                        if min_num <= new_number <= max_num and new_number in prime_set:
                            new_primes.append(new_number)
                    # If we have 8 or more primes, we're done
                    if len(new_primes) >= 8:
                        end_time = time() - start_time
                        print(base_prime, 'yields', new_primes, 'in', end_time, 'sec')
                        exit()

        # We have exhausted the current prime list and need a new one
        last_prime = base_prime
        sieve_end = (sieve_end * 10) + 9
