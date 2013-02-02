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
#  The most recent version of this program is available at:
#  http://github.com/Falcorian/Project-Euler-Solutions

from time import time
from optparse import OptionParser
from math import sqrt,floor

""" The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=500, help="find the first triangle number with NUM factores")

(options, args) = parser.parse_args()

# Functions
def returnFactors(num):
    """ Returns the factors of a number as a list """
    fnum = float(num)
    max = int(floor(sqrt(fnum)))
    factors = []
    for i in range(1,max+1):
        if not num%i:
            fact1 = i
            fact2 = num / i
            if fact1 == fact2:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(num / i)

    return factors

# Solution
s = time()

i = 1
while True:
    tri = (i * (i+1))/2 
    factors = returnFactors(tri)
    length = len(factors)
    #print str(tri)+':',length
    if length >= options.num:
        print tri,'in',time()-s,'secs'
        exit()
    i += 1
