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
from numpy import array, ceil, floor, sqrt, bool, nonzero, ones
"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.

n   Relatively Prime    phi(n)    n/phi(n)
2   1                   1         2
3   1,2                 2         1.5
4   1,3                 2         2
5   1,2,3,4             4         1.25
6   1,5                 2         3
7   1,2,3,4,5,6         6         1.1666...
8   1,3,5,7             4         2
9   1,2,4,5,7,8         6         1.5
10  1,3,7,9             4         2.5

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000000, help="find the last ten digits of the sum n**n")

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

    return nonzero(isPrime)[0] # Return the index values of True, that is primes

def returnUniquePrimeFactors(num):
    """ Return the unique prime factors of a number """
    onum = num
    primes = returnPrimes(num) # Get all the primes smaller than num
    primeFactors = []
    for prime in primes: 
        if not num % prime: 
            primeFactors.append(prime) # Only append the first time
            while num%prime !=0: # While we can still evenly divide the prime out, do so
                num = num/prime
        if num == 1:
            break
    if primeFactors == []: # The number must be prime! Return itself
        #print onum,[int(num)]
        return array([int(num)])
    else:
        #print onum,primeFactors
        return array(primeFactors)

def returnPrimeFactors(num):
    """ Return the prime factors of a number """
    onum = num
    primes = returnPrimes(num) # Get all the primes smaller than num
    num = float(num)
    primeFactors = []
    for prime in primes: 
        if not num % prime: 
            while not num%prime: # While we can still evenly divide the prime out, do so
                primeFactors.append(prime)
                num = num/prime
    if primeFactors == []: # The number must be prime! Return itself
        #print onum,[int(num)]
        return array([int(num)])
    else:
        #print onum,primeFactors
        return array(primeFactors)
        
def returnEulerTotient(num):
    """ Returns Euler's Totient of num, the number of numbers coprime with num """
    if num == 1 or num == 0:
        return 1 # 1 is the only number coprime to itself by definition; phi(0) := 1
    else:
        product = num
        primes = returnUniquePrimeFactors(num)
        primes = (1 - (1./primes))
        for prime in primes:
            product *= prime
        return product

# Solution
s = time.time()

maxnum = 0
maxi   = 0

for i in range(2,options.num+1):
    et = int(floor(returnEulerTotient(i))) # Mostly we get n.0, but sometimes we get some floating point. From a test of a few of them floor seems to provide the correct answer
    num = float(i)/et
    if i%1000 == 0:
        print i,'in',time.time()-s,'secs'
    if num > maxnum:
        maxnum = num
        maxi   = i

print maxi,'in',time.time()-s,'secs'
