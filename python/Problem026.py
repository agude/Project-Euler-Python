#  Copyright (C) 2011  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
from decimal import getcontext,Decimal
from numpy import array, ceil, floor, sqrt, bool, nonzero, ones, int64
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="max", default=1000, help="find the longest cycle of 1/d for d less than or equal to MAX")

(options, args) = parser.parse_args()

# Constants
max = options.max
getcontext().prec = 2*max # The cycles will be, at max, the size of the number - 1.

# Functions
def getCycleEvent(num,v=False):
    """
    Finds the length of a repeating cycle.
    """
    num = str(num)
    # Test for decimal
    try:
        if not num[1] == '.':
            return 0
    except IndexError:
        return 0
    ## Matching points
    num = num[2:] # Trimming off '0.'
    end = len(num)-1
    maxspacing = end/2
    for spacing in xrange(1,maxspacing):
        matches = 0
        t = 0
        h = t + spacing
        while h <= end:
            if t >= end or h >= end: # No cycles
                break
            tort = num[t]
            hare = num[h]
            if tort == hare:
                matches += 1
            t += 1
            h += 1
        if matches/float(end) > .45:
            return spacing

def returnPrimes(num):
    """
    Return a list of primes up to num
    """
    isPrime = ones(num,dtype=bool) # An array of bools to test using their index
    isPrime[0] = isPrime[1] = 0 # 0,1 not prime
    for i in xrange(2,int(ceil(sqrt(num)))):
        if isPrime[i]: # False if already proven not prime
            # Starting at i*i : until the end of the array : incriment by i
            # You can start at i*i because lower mutliples have already been removed
            isPrime[i*i:num+1:i] = False

    return array(nonzero(isPrime)[0],dtype=int64) # Return the index values of True, that is primes

# Solution
s = time.time()

## We look only at primes. If n has a cycle of length m, then so do all
## multiples of n. Therefore only primes have a chance at a new cycle length.
primes = returnPrimes(max)
maxcyclen = 0
d = 0
## We start at the end as the maximum cycle length is number - 1
for i in primes[::-1]:
    # Cycle is larger then remaining numbers, so their cycles must be shorter
    if maxcyclen >= i:
        break 
    num = Decimal(1)/Decimal(i)
    cyclen = getCycleEvent(num,v=False)
    if cyclen > maxcyclen:
        maxcyclen = cyclen
        d = i

print d,'in',time.time()-s,'secs'
