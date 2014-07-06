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
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by canceling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

# Only runs if executed directly
if __name__ == '__main__':
    from fractions import Fraction
    from time import time

    # Solution
    start_time = time()

    # We brute force the solution. Since we know that two of the numbers must
    # cancel, we only need three loops to make the four digits.
    total_numerator = 1
    total_denominator = 1
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                numerator = 10 * i + j
                denominator = j * 10 + k
                # If cancellation would make them then multiplying by the
                # inverse of the reduced fraction, that is k/i, would give us
                # 1, that is the new numerator and new denominator should be
                # equal.
                if numerator < denominator and numerator * k == denominator * i:
                    total_numerator *= numerator
                    total_denominator *= denominator
                    print("Faction found:", numerator, "/", denominator)

    # We use Fraction to reduce our answer
    fraction = Fraction(total_numerator, total_denominator)

    end_time = time() - start_time
    print(fraction, 'in', end_time, 'secs')
