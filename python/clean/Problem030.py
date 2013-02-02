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

""" Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4
    As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""

from time import time
from optparse import OptionParser

# Optparse setup
usage = "usage: %prog [OPTIONS] -n NUM"
parser = OptionParser(usage=usage)
parser.add_option("-n", action="store", type="int", dest="NUM", default=5, help="find the sum of all numbers that are the sum of their digits to the NUM power")

(options, args) = parser.parse_args()

# Functions
def get_powers(pow):
    """ Returns a dictionary of all digits raised to pow.  """
    powdict = {}
    for i in xrange(10):
        powdict[str(i)] = i**pow
    return powdict

def is_sum_of_digits(num,powdict):
    """ Returns True if num is equal to the the sum of its digits raised to the power specificed in powdict.

    """
    if num < 2 or int(num) != float(num): # negative, 0, 1, and floats don't count
        return False
    else:
        newnum = sum([powdict[i] for i in str(num)])
        if newnum == num:
            return True
        else:
            return False

# Constants
POW = options.NUM

# Solution
s = time()

# Create a mapping of digits to power to speed the process
powdict = get_powers(POW)

max = 9**POW
total = 0
i=0
while True:
    if is_sum_of_digits(i,powdict):
        total += i
    i += 1
    # At some point the numbers become larger than their digits could possibly
    # sum to. When we reach this point we know that we have exhaustively
    # searched the possible problem space, and so halt.
    if max*len(str(i)) <= i:
        break

print total,'in',time()-s,'secs' 
