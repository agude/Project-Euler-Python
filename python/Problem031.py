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
In England the currency is made up of pound, $, and pence, p, and there are
eight coins in general circulation:

    1p,  2p,  5p,  10p,  20p,  50p,  $1 (100p) and $2 (200p).

It is possible to make $2 in the following way:

    1 * $1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can $2 be made using any number of coins?
"""


# Functions
def coin_value(ones=0, twos=0, fives=0, tens=0, twenties=0, fifties=0,
               pounds=0, twopounds=0):
    """ Return the total value for a set of coins. """
    total = 0
    total += ones
    total += (twos * 2)
    total += (fives * 5)
    total += (tens * 10)
    total += (twenties * 20)
    total += (fifties * 50)
    total += (pounds * 100)
    total += (twopounds * 200)
    return total

# Only runs if executed directly
if __name__ == '__main__':
    from time import time
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=200, help="find number of ways to make NUM pence with British coins")

    (options,  args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    # Solution
    # First we find the maximum of each type
    start_time = time()
    max1 = NUM

    # Then we loop over possible combinations
    combos = 0
    for ones in range(0, max1 + 1):
        amount = coin_value(ones)
        max2 = (NUM - amount) // 2
        for twos in range(0, max2 + 1):
            amount = coin_value(ones, twos)
            max5 = (NUM - amount) // 5
            for fives in range(0, max5 + 1):
                amount = coin_value(ones, twos, fives)
                max10 = (NUM - amount) // 10
                for tens in range(0, max10 + 1):
                    amount = coin_value(ones, twos, fives, tens)
                    max20 = (NUM - amount) // 20
                    for twents in range(0, max20 + 1):
                        amount = coin_value(ones, twos, fives, tens, twents)
                        max50 = (NUM - amount) // 50
                        for fifts in range(0, max50 + 1):
                            amount = coin_value(ones, twos, fives, tens,
                                                twents, fifts)
                            max100 = (NUM - amount) // 100
                            for hunds in range(0, max100 + 1):
                                amount = coin_value(ones, twos, fives, tens,
                                                    twents, fifts, hunds)
                                max200 = (NUM - amount) // 200
                                for twohunds in range(0, max200 + 1):
                                    amount = coin_value(ones, twos, fives,
                                                        tens, twents, fifts,
                                                        hunds, twohunds)
                                    if amount == NUM:
                                        combos += 1

    end_time = time() - start_time
    print(combos, 'in', end_time, 'secs')
