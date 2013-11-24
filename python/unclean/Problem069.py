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
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
from time import time
from optparse import OptionParser
from numpy import array, ceil, floor, sqrt, bool, nonzero, ones, int64
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
usage = "usage: %prog [OPTIONS] -n number -b"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000000, help="find the max of n/phi(n) for 0 < n < NUM+1")
parser.add_option("-b", "--brute", action="store_true", dest="brute", default=False, help="if true, use a brute force calculate n/phi(n). VERY SLOW!")

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

def returnPrimeFactors(num,inputPrimes=[]):
    """ 
    Return the prime factors of a number in a dictionary


    {primeFactor1:n1,primeFactor2:n2....}
    """
    onum = num

    if inputPrimes == []: # If we got an empty list, make the list
        inputPrimes = returnPrimes(num+1) # Get all the primes up to num

    if num in inputPrimes: # The number is prime! Return itself
        return {onum:1}

    primeFactors = {}
    for prime in inputPrimes: 
        if not num % prime and num != 1: 
            primeFactors[prime] = 1
            num = num/prime
            while not num%prime and num != 1: # While we can still evenly divide the prime out, do so
                primeFactors[prime] += 1
                num = num/prime
        if num == 1:
            break

    #print onum,primeFactors
    return primeFactors
        
def returnEulerTotient(num,inputPrimes=[]):
    """ 
    Returns Euler's Totient of num, the number of numbers coprime with num

    From Wikipedia:
    
    phi(n) = (p1 - 1)*(p1**(k1-1)) 
    where p1 is a prime factor of n, and k1 is the frequency of that prime factor
    """
    if num == 1 or num == 0:
        return 1 # 1 is the only number coprime to itself by definition; phi(0) := 1
    else:
        product = 1
        primes = returnPrimeFactors(num,inputPrimes)
        for prime in primes:
            k = primes[prime]
            product *= (prime - 1)*(prime**(k-1))
        return product

# Solution
s = time()

maxnum = 0
maxi   = 0
num    = options.num
brute  = options.brute

if brute:
    inputPrimes = returnPrimes(num+1)

    for i in range(2,num+1):
        et = returnEulerTotient(i,inputPrimes)
        num = float(i)/et
        if num > maxnum:
            maxnum = num
            maxi   = i

else:
    """
    n/phi(n) = Product[ p / ( p - 1 ) ] over the unique primes that divide n.

    Then n/phi(n) is maximal if n is the product of the first k prime numbers.
    """
    products = []
    runningProduct = 1

    startPrimes = 10000 # Just a nice big number... 
    inputPrimes = returnPrimes(startPrimes)

    for i in range(len(inputPrimes)):
        runningProduct *= int(inputPrimes[i]) # Int64 from Numpy Vs. Python BigInt again....
        if runningProduct > num:
            break
        else:
            products.append(runningProduct)
    maxi = max(products)

print maxi,'in',time()-s,'secs'
