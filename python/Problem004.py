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
""" A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -m MAX -n MIN"
parser = OptionParser(usage=usage)
parser.add_option("-m", "--max", action="store", type="int", dest="MAX", default=999, help="find a palindromic number by multipling numbers <= MAX")
parser.add_option("-n", "--min", action="store", type="int", dest="MIN", default=100, help="find a palindromic number by multipling numbers >= MIN")

(options, args) = parser.parse_args()

# Functions
def isPalindromic(num):
    """ Returns True if num is palindromic, False otherwise.

    Keyword arguments:
    num  -- test if num is palindromic

    """
    num = str(num)

    for i in xrange(len(num) / 2):
        if int(num[i]) != int(num[-(i+1)]):
            return False

    return True

# Constants
MAX = options.MAX
MIN = options.MIN

# Solution
s = time()

num = 0
for a in xrange(MAX,MIN-1,-1):
    for b in xrange(a,MIN-1,-1):
        num = a*b
        if isPalindromic(num):
            break # First one is largest

print num,'in',time()-s,'secs' 
