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
#  The most recent version of this program is avaible at:
#  http://github.com/Falcorian/Project-Euler-Solutions

from time import time
from optparse import OptionParser
""" The sum of the squares of the first ten natural numbers is:
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n MAX"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--max", action="store", type="int", dest="MAX", default=100, help="find (1**2 + 2**2 + ... + MAX**2) - (1 + 2 + ... + MAX)**2")

(options, args) = parser.parse_args()

# Constants
MAX = options.MAX

# Solution
s = time()

x = 0
x2 = 0
for i in xrange(MAX+1): # We just brute force it
    x += i
    x2 += i*i

print "(",x*x,"-",x2,") =",(x*x - x2),'in',time()-s,'secs'
