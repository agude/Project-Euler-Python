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
from math import sqrt,floor
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="max", default=10001, help="find number'th prime")

(options, args) = parser.parse_args()

# Functions
#def isprime(num):
#    """ Is number prime? Returns bool. """
#    if num <= 1 or int(num) != float(num): # 0,1, negative numbers, and floats are not prime
#        return False
#    elif num == 2: # 2 is prime
#        return True
#    else:
#        root = int(ceil(sqrt(num)))
#        for i in range(2,root+1):
#            if not num%i:
#                break
#        else:
#            return True
#
#        return False

def isprime(num):
    """ Is number prime? Returns bool. """
    if num < 1 or int(num) != float(num): # 0,1, negative numbers, and floats are not prime
        return False
    elif num < 4:
        return True # 2,3 are prime, others already excluded
    elif not num%2:
        return False
    elif num < 9: # We have now excluded 4,6,8
        return True
    elif not num%3:
        return False
    else:
        r = floor(sqrt(num))
        f = 5
        while f <= r:
            if not num%f:
                return False
            elif not num%(f+2):
                return False
            else:
                f += 6
        else:
            return True

# Solution
s = time.time()

mx = options.max

i = 3 # Starting at first prime
primes = [2]
while len(primes) < mx:
    if isprime(i):
        primes.append(i)
    i += 2

print primes[-1],'in',time.time()-s,'secs'
