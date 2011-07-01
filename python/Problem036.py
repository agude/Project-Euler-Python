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
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n","--num", action="store", type="int", dest="num", default=1000000, help="sum all numbers less than NUM that are palindromic in base 10 and base 2")

(options, args) = parser.parse_args()

# Functions
def isPalindromic(num):
    """ Returns True/False after checking if num is palindromic """
    num = str(num)

    for i in range(len(num) / 2):
        if int(num[i]) != int(num[-(i+1)]):
            return False
    
    return True

# Constants
max = options.num
nums = []

# Solution
s = time()

for i in xrange(1,max):
    if isPalindromic(i):
        b = bin(i)[2:] # Need to cut off "0b"
        if isPalindromic(b):
            nums.append(i)
#            print i,b

print sum(nums),'in',time()-s,'secs' 
