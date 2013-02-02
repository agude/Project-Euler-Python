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
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  The most recent version of this program is available at:
#  http://github.com/Falcorian/Project-Euler-Solutions

from time import time
from optparse import OptionParser
from numpy import array, ceil, floor, sqrt, bool, nonzero, ones, int64
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000000, help="find the number of circular primes below NUM.")

(options, args) = parser.parse_args()

# Functions
def returnPrimes(num):
    """ Return a list of primes up to num """
    isPrime = ones(num,dtype=bool) # An array of bools to test using their index
    isPrime[0] = isPrime[1] = 0 # 0,1 not prime
    for i in xrange(2,int(ceil(sqrt(num)))):
        if isPrime[i]: # False if already proven not prime
            # Starting at i*i : until the end of the array : incriment by i
            # You can start at i*i because lower mutliples have already been removed
            isPrime[i*i:num+1:i] = False

    return array(nonzero(isPrime)[0],dtype=int64) # Return the index values of True, that is primes

def returnCirculars(num):
    """
    Returns a list of the circular permutations of num
    """
    nums = []
    snum = str(num)
    lens = len(snum)
    if lens == 1:
        return [num]
    else:
        for i in range(len(snum)):
            newnum = []
            for j in range(len(snum)):
                newnum.append(snum[(i+j)%lens])
            newn = int(''.join(newnum))
            if newn not in nums:
                nums.append(newn)
    return nums

# Solution
s = time()

num = options.num
inputPrimes = returnPrimes(num+1)
outputPrimes = []

for prime in inputPrimes:
    # Don't double count
    if prime in outputPrimes:
        continue
    # Test if all permutations are prime
    else:
        circs = returnCirculars(prime)
        allprime = True
        for cir in circs:
            if cir not in inputPrimes:
                allprime = False
                break
        if allprime:
            outputPrimes = outputPrimes + circs

outputPrimes.sort()
print len(outputPrimes),'in',time()-s,'secs'
