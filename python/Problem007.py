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

""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?

"""

from time import time
from optparse import OptionParser
from numpy import array, bool, nonzero, ones, int64
from math import ceil, sqrt, log

# Optparse setup
usage = "usage: %prog [OPTIONS] -n NUM"
parser = OptionParser(usage=usage)
parser.add_option("-n", action="store", type="int", dest="NUM", default=10001, help="find the NUM'th prime")

(options, args) = parser.parse_args()

# Functions
def get_primes(num):
    """ Return an array of primes below num.

    Keyword arguments:
        num  -- find primes below this number

    """
    isPrime = ones(num,dtype=bool) # An array of bools to test using their index
    isPrime[0] = isPrime[1] = False # 0,1 not prime
    for i in xrange(2,int(ceil(sqrt(num)))):
        if isPrime[i]: # False if already proven not prime
            # Starting at i*i : until the end of the array : incriment by i
            # You can start at i*i because lower mutliples have already been removed
            isPrime[i*i:num+1:i] = False

    return array(nonzero(isPrime)[0],dtype=int64) # Return the index values of True, that is primes

# Constants
NUM = options.NUM

# Solution
s = time()

# We need an upper bound on the prime to use the fast sieve
if NUM >=6:
    # P_n <= n * log(n) + n log(log(n))
    MAX = NUM * log(NUM) + NUM * log(log(NUM))
    primes = get_primes(MAX)
elif NUM > 0:
    primes = [2, 3, 5, 7, 11, 13]
else:
    primes = None

if primes is not None:
    print primes[NUM-1],'in',time()-s,'secs'
else:
    print primes,'in',time()-s,'secs'
