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
from math import factorial
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
# Optparse setup
#usage = "usage: %prog [OPTIONS] -a number -b number"
#parser = OptionParser(usage=usage)
#parser.add_option("-a", "--amax", action="store", type="int", dest="amax", default=100, help="calculate a^b for 2 < a < amax")
#parser.add_option("-b", "--bmax", action="store", type="int", dest="bmax", default=100, help="calculate a^b for 2 < b < bmax")

#(options, args) = parser.parse_args()

# Functions
def isDigitFactorial(num):
    """ Returns true of the sum of the factorial of digits is equal to the number, else false """
    if num < 10: # 1! and 2! do not count
        return False
    else:
        sum = 0
        for i in range(len(str(num))):
            sum += factorial(int(str(num)[i]))
            if sum > num:
                return False
        if sum == num:
            return True
        else:
            return False

# Solution
s = time()

nsum = 0
for i in range(50000):
    if isDigitFactorial(i):
        nsum += i

print nsum,'in',time()-s,'secs'
