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
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy and only
277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?
"""

from euler.combinatorics import n_choose_k
from time import time


def problem_113(num=100):
    start_time = time()

    # This can only be done with combinatorics.
    #
    #
    # First we consider the case of increasing numbers:
    #
    # The first digit is, a, allowed to be 0 to 9 (0-9), the second digit, b,
    # is allowed to be a-9, the third digit, c, is allowed to b-9, etc. It is
    # allowed that a = b = c.
    #
    # This allows us to pick from a pool of 10 + (n - 1) digits for an n digit
    # string because we can choose 0-9, and n - 1 may be duplicates of the
    # previously chosen number. Then we have 9 + N digits to select from, and 9
    # to select. We note that, while leading 0s are allowed (as 012 = 12 is an
    # increasing number), 0 itself is not an allowed number, so we subtract 1.
    #
    # This means the number of increasing numbers is:

    number_increasing = n_choose_k(num + 9, 9) - 1

    # We consider a similar argument for decreasing numbers:
    #
    # The first digit, a, can be 0-9, the second digit, b, is allowed to be
    # 0-a, the third digit, c, is allowed to be 0-b, etc, where we define the
    # range notation 0-0 to mean 0-9. We again may select from 10 + (n - 1)
    # digits, but we note that this doesn't account for numbers of the form
    # 091, and so add an additional digit to allow for the leading 0, giving us
    # 10 + N digits.
    #
    # Again 0 is not an allowed number, so we subtract 1 from the final total.
    # In this case however, we also introduce another n copies of 0 by allowing
    # the first digit to be 0, so we subtract off another n.
    #
    # This means the number of increasing numbers is:

    number_decreasing = n_choose_k(num + 10, 10) - (num + 1)

    # Double counting is much easier to account for. All double counted number
    # have the form where every digit is the same. Since there are exactly 9 of
    # these per power of 10, we subtract 9 * n.

    double_counting = 9 * num

    # We add the number of increasing and decreasing numbers, and subtract the
    # number double counted
    answer = number_increasing + number_decreasing - double_counting

    end_time = time() - start_time

    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="NUM", default=100, help="find the number of bouncy numbers below 10**n")

    (options, args) = parser.parse_args()

    # Constants
    NUM = options.NUM

    problem_113(NUM)
