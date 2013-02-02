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

from time import time
from optparse import OptionParser
from math import sqrt,floor
"""
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-a", "--amax", action="store", type="int", dest="amax", default=1000, help="enforce a < amax in n**2 + an + b")
parser.add_option("-b", "--bmax", action="store", type="int", dest="bmax", default=1000, help="enforce b < bmax in n**2 + an + b")

(options, args) = parser.parse_args()

# Functions
def isPrime(num):
    """ Is number prime? Returns bool. """
    if num < 2 or int(num) != float(num): # 0,1, negative numbers, and floats are n
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
s = time()

best = 0
besta= 0
bestb= 0
for a in range(-options.amax,options.amax+1):
    for b in range(-options.bmax,options.bmax+1):
        cons = 0
        n = 0
        while isPrime( n*n + a*n + b ):
            cons += 1
            n += 1
        if cons > best:
            #print cons,a,b
            besta = a
            bestb = b
            best  = cons

print 'Longest series goes to n =',best,'with a =',besta,'and b =',bestb,' and a*b = ',besta*bestb,'in',time()-s,'secs'
