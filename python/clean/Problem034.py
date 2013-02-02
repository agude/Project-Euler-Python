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

""" 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

from time import time
from optparse import OptionParser
from math import factorial

# Optparse setup
usage = "usage: %prog"
parser = OptionParser(usage=usage)

(options, args) = parser.parse_args()

# Functions
def is_digit_factorial(num):
    """ Returns true if the sum of the factorial of digits is equal to the number, else false """
    if num < 10: # 1! and 2! do not count
        return False
    else:
        sum = 0
        snum = str(num)

        if num > 362880:
            pass
        elif num <= 362880 and '9' in snum:
            return False
        elif num >40320:
            pass
        elif num <= 40320 and '8' in snum:
            return False
        elif num > 5040:
            pass
        elif num <= 5040 and '7' in snum:
            return False
        elif num > 720:
            pass
        elif num <= 720 and '6' in snum:
            return False
        elif num > 120:
            pass
        elif num <= 120 and '5' in snum:
            return False
        elif num > 24:
            pass
        elif  num <= 24 and '4' in snum:
            return False

        for i in snum:
            sum += factorial(int(i))
            if sum > num:
                return False
        if sum == num:
            return True
        else:
            return False

# Solution
s = time()

nsum = 0
for i in xrange(500000):
    if is_digit_factorial(i):
        nsum += i

print nsum,'in',time()-s,'secs'
