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
"""The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

"""
# Optparse setup
usage = "usage: %prog [OPTIONS]"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--num", action="store", type="int", dest="num", default=1000000, help="")

(options, args) = parser.parse_args()

# Classes

# Functions
def return_primes(num):
    """Return a list of primes up to num"""
    isPrime = ones(num,dtype=bool) # An array of bools to test using their index
    isPrime[0] = isPrime[1] = 0 # 0,1 not prime
    for i in xrange(2,int(ceil(sqrt(num)))):
        if isPrime[i]: # False if already proven not prime
            # Starting at i*i : until the end of the array : incriment by i
            # You can start at i*i because lower mutliples have already been removed
            isPrime[i*i:num+1:i] = False

    return array(nonzero(isPrime)[0],dtype=int64) # Return the index values of True, that is primes

def returnPrimeDict(primes,max):
    """ Return a dictionary of the form {0:False,1:False,2:True,....} """
    primedict = {}
    oldprime = -1
    for prime in primes:
        primedict[prime] = True
        for i in range(oldprime+1,prime):
            primedict[i] = False
            oldprime = prime
    for i in range(oldprime+1,max):
        primedict[i] = False
    return primedict

# Constants
max = options.num

# Solution
s = time.time()

## Get our primes
primes = return_primes(max+1)
primedict = returnPrimeDict(primes,max+1)
lenprime = len(primes)

## Find the largest length of primes we could possibly add to set upper bound
tot = 0
for i in xrange(lenprime):
    tot += primes[i] 
    if tot <= max:
        maxlen = i
    else:
        break

## Try to make primes
bestlen = 0
bestprime = 0
for length in range(2,maxlen)[::-1]:
    if length < bestlen:
        break
    for start in xrange(0,lenprime-length+1):
        testnum = sum(primes[start:start+length])
        if testnum > max:
            break
        if primedict[testnum] and length > bestlen:
            print testnum,primes[start:start+length]
            bestlen = length
            bestprime = testnum

print 'in',time.time()-s,'secs'
