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

from time import time
from optparse import OptionParser
from itertools import count,islice
""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n NUM"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--num", action="store", type="int", dest="NUM", default=10001, help="find NUM'th prime")

(options, args) = parser.parse_args()

# Functions
def prime_iter():
    """ Return an iterator over primes. """
    not_primes = {}
    yield 2 # Only even prime, put in by hand
    for i in islice(count(0),3,None,2):
        j = not_primes.pop(i, None) # If i is alread in not_primes, remove and return it, otherwise return None
        if j is None:
            yield i
            not_primes[i*i] = i
        else:
            k = i+j
            while k in not_primes or not k%2: #If k will be knocked out by a smaller multiple, we ignore it and continue
                k += j
            not_primes[k] = j

# Constants
NUM = options.NUM

# Solution
s = time()

for prime in islice(prime_iter(),NUM-1,NUM,1):
    pass

print prime,'in',time()-s,'secs'
