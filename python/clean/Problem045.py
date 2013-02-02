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

""" Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle        Tn=n(n+1)/2      1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n-1)/2     1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n-1)       1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

"""

from time import time
from optparse import OptionParser
from math import sqrt

# Optparse setup
usage = "usage: %prog [OPTIONS]"
parser = OptionParser(usage=usage)

(options, args) = parser.parse_args()

# Functions
def is_hex(num):
    """
    Returns true if num is Hexagonal. That is num = n*(2n-1) for sum integer n.
    """
    testnum = ( sqrt( (8*num) + 1 ) + 1 ) / 4
    if int(testnum) == float(testnum): # Test for int
        return True
    else:
        return False

def is_pent(num):
    """
    Returns true if num is Pentagonal. That is num = n*(3n-1)/2 for sum integer n.
    """
    testnum = ( sqrt( (24*num) + 1 ) + 1 ) / 6
    if int(testnum) == float(testnum): # Test for int
        return True
    else:
        return False

# Solution
s = time()

# Compute Hexoginal numbers as there are fewer. We note that all hexoginal numbers are triangle numbers.
n = 144 # Starting number is h144
while True:
    num = n*(2*n-1)
    if is_pent(num):
        break
    else:
        n += 1

print num,n,'in',time()-s,'secs' 
