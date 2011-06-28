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
from numpy import array, ceil, floor, sqrt, bool, nonzero, ones, int64
""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 317584931803?

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n NUM"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--NUM", action="store", type="int", dest="num", default=317584931803, help="find the largest prime factor of NUM")

(options, args) = parser.parse_args()

# Functions
def get_primes(num):
    """ Returns an array of primes below num.

    Keyword arguments:
        num  -- find primes below this number

    """
    isPrime = ones(num,dtype=bool) # An array of bools to test using their index
    isPrime[0] = isPrime[1] = 0 # 0,1 not prime
    for i in xrange(2,int(ceil(sqrt(num)))):
        if isPrime[i]: # False if already proven not prime
            # Starting at i*i : until the end of the array : incriment by i
            # You can start at i*i because lower mutliples have already been removed
            isPrime[i*i:num+1:i] = False

    return array(nonzero(isPrime)[0],dtype=int64) # Return the index values of True, that is primes

# Constants
NUM = options.num

# Solution
s = time.time()

MAX = int(ceil(sqrt(NUM))) + 1
primes = get_primes(MAX)

maxprime = 0

for prime in primes:
    while not NUM%prime:
        maxprime = prime
        NUM = NUM/prime

print maxprime,'in',time.time()-s,'secs' 
