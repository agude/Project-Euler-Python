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
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS]"
parser = OptionParser(usage=usage)

(options, args) = parser.parse_args()

# Functions
def returnProperFactorsSum(num):
    """ Returns the sum of proper factors of a number """
    fnum = float(num)
    max = int(floor(sqrt(fnum)))
    factors = []
    for i in range(1,max+1):
        if not num%i:
            fact1 = i
            fact2 = num / i
            if fact1 == fact2:
                if i != num:
                    factors.append(i)
            else:
                if (num/i) != num:
                    factors.append(num / i)
                if i != num:
                    factors.append(i)

    return sum(factors)

# Constants
max = 28123 # All numbers > 28123 are the sum of two abundant

# Solution
s = time()

## Generate abundant numbers
abundant = []
check = {} # Using {1:False, ..., 12: True, ...} to test if a number is abundant is MUCH faster than "if num in abundant"
for i in xrange(0,max+2): 
    if returnProperFactorsSum(i) > i:
        abundant.append(i)
        check[i] = True
    else:
        check[i] = False

## Check numbers
notsum = []
for i in xrange(1,max+1):
    add = True
    for j in abundant:
        if j >= i: # If we're here, it passes our criteria and we add it
            notsum.append(i)
            break
        if check[i-j]: # Sum of two abundant, reject
            break

print sum(notsum),'in',time()-s,'secs' 
