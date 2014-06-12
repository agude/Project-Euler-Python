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
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

def is_pandigital(number):
    test_numbers = []
    str_number = str(number)
    for i in range(1, len(str_number) + 1):
        test_numbers.append(str(i))

    for digit in test_numbers:
        if digit not in str_number:
            return False

    return True

# Only runs if executed directly
if __name__ == '__main__':
    from math import factorial, floor
    from optparse import OptionParser
    from time import time
    from euler.primes import prime_sieve
    from sys import exit

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NTH", default=9, help="find the largest n-digit pandigital prime")

    (options, args) = parser.parse_args()

    # Read in options
    NTH = options.NTH

    # The maximum number to check has NTH digits, and has digits from left to
    # right of:
    # N N-1 ... 1
    num_list = []
    for i in range(NTH, 0, -1):
        num_list.append(str(i))
    MAX_NUM = int(''.join(num_list))

    # Solution
    start_time = time()

    primes = prime_sieve(MAX_NUM)
    print(len(primes), "primes found!")

    answer = None
    i = 0
    for test_num in reversed(primes):
        if not i % 1000:
            print(i)
        i += 1
        if is_pandigital(test_num):
            answer = test_num
            break

    end_time = time() - start_time

    print(answer, 'in', end_time, 'secs')
