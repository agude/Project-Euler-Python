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
Nim is a game played with heaps of stones, where two players take it in turn to
remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as
follows:
    - At the start of the game there are three heaps of stones.
    - On his turn the player removes any positive number of stones from any
      single heap.
    - The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and
n3 then there is a simple function X(n1,n2,n3) -- that you may look up or
attempt to deduce for yourself -- that returns:
    * zero if, with perfect strategy, the player about to move will eventually
      lose; or
    * non-zero if, with perfect strategy, the player about to move will
      eventually win.

For example X(n1, n2, n3)=0 because, no matter what the current player does,
his opponent can respond with a move that leaves two heaps of equal size, at
which point every move by the current player can be mirrored by his opponent
until no stones remain; so the current player loses. To illustrate:
    - current player moves to (1, 2, 1)
    - opponent moves to (1, 0, 1)
    - current player moves to (0, 0, 1)
    - opponent moves to (0, 0, 0), and so wins.

For how many positive integers n <= 2**30 does X(n, 2n, 3n) = 0 ?
"""

from time import time


def problem_301(max_num=2**30):
    start_time = time()

    # There is nothing elegant here, we simply brute force
    total = 0
    for a in range(1, max_num + 1):
        if not (a ^ (a * 2) ^ (a * 3)):
            total += 1

    end_time = time() - start_time
    print(total, "in", end_time, "secs")
    return total


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", type="int", dest="MAX", default=2**30, help="find the number of losing nim games up to NUM")

    (options, args) = parser.parse_args()

    # Constants
    MAX = options.MAX

    problem_301(MAX)
