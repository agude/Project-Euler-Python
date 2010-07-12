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
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=10000, help="find the sum of all amicable numbers under NUM")

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

# Solution
s = time.time()

num = options.num
pairs = []

for i in range(num):
    if i not in pairs: # No repeats
        checkNum = returnProperFactorsSum(i)
        if checkNum > i: # If not true, we would have found it already
            if (returnProperFactorsSum(checkNum) == i) and (i != checkNum): # Perfect numbers (like 6) are not included
                #print i,checkNum
                pairs.append(i)
                pairs.append(checkNum)

print sum(pairs),'in',time.time()-s,'secs'
