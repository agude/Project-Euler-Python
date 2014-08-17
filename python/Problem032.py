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

""" We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from euler.converter import int_to_tuple, iterable_to_int
    from euler.pandigital import pandigitals
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS] -n MAX"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="DIGITS", default=9, help="check only pandigital numbers with this number of digits")

    (options, args) = parser.parse_args()

    # Constants
    DIGITS = options.DIGITS

    # Solution
    start_time = time()

    # We make a list of every single pandigital number with the requested
    # number of  digits or less, and all of the number - 1 or less. We subtract
    # the sets to get only pandigitals with the right number of digits.
    products = set([])
    all_pandigitals = set(pandigitals(maximum_digits=DIGITS))
    some_pandigitals = set(pandigitals(maximum_digits=DIGITS-1))
    pandigitals_to_check = all_pandigitals - some_pandigitals
    # For each 9 digit pandigital we check every possible combination of
    # multiplicand, multiplier, and product by moving the * and = through the
    # number from left to right, insure that the = is always ahead of the *
    # symbol, and that each of the multiplicand, multiplier, and product have
    # at least 1 digit. We use a set to keep only unique products.
    for number in pandigitals_to_check:
        number_tuple = int_to_tuple(number)
        end_point = len(number_tuple)
        for times_position in range(1, end_point):
            for equals_position in range(times_position + 1, end_point):
                multiplicand_tuple = number_tuple[:times_position]
                multiplicand = iterable_to_int(multiplicand_tuple)
                multiplier_tuple = number_tuple[times_position:equals_position]
                multiplier = iterable_to_int(multiplier_tuple)
                product_tuple = number_tuple[equals_position:]
                product = iterable_to_int(product_tuple)
                if multiplicand * multiplier == product:
                    print(multiplicand, "*", multiplier, "==", product)
                    products.add(product)

    # Finally we compute the required sum
    answer = sum(products)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
