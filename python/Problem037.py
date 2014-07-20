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
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

if __name__ == '__main__':
    from time import time
    from euler.primes import is_left_truncatable_prime as is_ltp
    from euler.primes import is_right_truncatable_prime as is_rtp

    # Right/Left Truncatable Primes (RTP/LTP) are a proper superset of
    # Truncatable Primes (TP). The union of RTP and LTP is equal to TP. The
    # size of RTP is much smaller than LTP, so we calculate that first, and
    # then find the union with LTP

    # Solution
    start_time = time()

    # All RTPs must end with a single digit prime
    starts = ('2', '3', '5', '7')
    # Anything even is divisible by 2, 5 is divisible by 5, 0 by both. This
    # leaves only 4 digits that RTPs can contain other than the base four
    # (which can only be the leftmost digit if they aren't also in this list).
    addons = ('1', '3', '7', '9')

    # Generate all RTP, excluding the single digit primes. We know that every
    # TP must be one digit from another TP, so take all the previously found
    # ones and try to find new ones by adding all of the possible digits.
    # Successful new TPs are added to the stack, and we know we've found them
    # all when the stack is empty.
    rights = set([])
    stack = set(starts)
    while stack:
        base = stack.pop()
        for n in addons:
            # Since these are string, the + concatenates them
            num = int(base + n)
            # If the number is an RTP, add it to the final list of RTPs, and to
            # the stack to generate more
            if is_rtp(num):
                rights.add(str(num))
                stack.add(str(num))

    # Find the members of right that are also left prime and sum them
    answer = sum([int(i) for i in rights if is_ltp(int(i))])

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
