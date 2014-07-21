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
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the
reverse and add process is called a Lychrel number. Due to the theoretical
nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise. In addition you are given that
for every number below ten-thousand, it will either (i) become a palindrome in
less than fifty iterations, or, (ii) no one, with all the computing power that
exists, has managed so far to map it to a palindrome. In fact, 10677 is the
first number to be shown to require over fifty iterations before producing a
palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel
numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
theoretical nature of Lychrel numbers.
"""

if __name__ == '__main__':
    from euler.converter import reverse_int
    from euler.palindromic import is_palindromic
    from optparse import OptionParser
    from time import time

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--max", action="store", type="int", dest="MAX", default=10000, help="the bound on the largest number to check")

    (options, args) = parser.parse_args()

    # Solution
    start_time = time()

    MAX = options.MAX

    lychrels = set([])
    not_lychrels = set([])
    for number in range(MAX):
        test_number = number
        # As we test numbers, we generate a whole series of "kin" numbers (the
        # pair of numbers from each iteration) which, if their "seed" is
        # lychrel, we know to be lychrel numbers themselves. Likewise, we
        # know that non-lychrel numbers produce kin which are in turn
        # non-lychrel numbers. We cache these to save time
        if test_number in lychrels or test_number in not_lychrels:
            continue

        number_of_attempts = 0
        potential_lychrels = set([])
        while number_of_attempts < 51:
            number_of_attempts += 1
            # Cache values, as explained above
            if test_number <= MAX:
                potential_lychrels.add(test_number)

            # We cache the reversed number only if
            # reverse_int(reverse_int(number)) == number. If they fail this,
            # then we are stripping off 0s in the reversal, and so risk adding
            # junk to our potential numbers.
            reversed_number = reverse_int(test_number)
            if (reversed_number <= MAX
                    and reverse_int(reversed_number) == test_number):
                potential_lychrels.add(reversed_number)

            # Complete the reverse and add process and test if the result is
            # palindromic, if it is the number is not a lynchrel number (and
            # neither are its kin), so add the numbers generated to the
            # not_lychrels set
            test_number += reversed_number
            if is_palindromic(test_number):
                not_lychrels = not_lychrels.union(potential_lychrels)
                break
        # The else clause only runs if we don't break, which means we have a
        # set of lychrel numbers
        else:
            lychrels = lychrels.union(potential_lychrels)

    answer = len(lychrels)

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
