#  Copyright (C) 2010  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
#  The most recent version of this program is avaible at:
#  http://github.com/Falcorian/Project-Euler-Solutions

import time
from optparse import OptionParser
"""
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000000, help="find the number that produces the longest chain searching from 0 to NUM")

(options, args) = parser.parse_args()

# functions
def returnChain(num):
    """ Returns the chain:
        n --> n/2 (n is even)
        n --> 3n + 1 (n is odd)
    """
    chain = [num]
    while num > 1:
        if num%2: # Odd
            num = num*3 + 1
        else:     # Even
            num = num/2
        chain.append(num)

    return chain

# Solution
s = time.time()

mxlen = 0
mxnum = 0
mxchain = 0
for num in range(0,options.num):
    chain = returnChain(num)
    lens = len(chain)
    if lens > mxlen:
        mxlen = lens
        mxnum = num
        mxchain = chain

print mxnum,'in',time.time()-s,'secs'
#print mxchain
