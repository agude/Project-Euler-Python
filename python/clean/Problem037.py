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
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  The most recent version of this program is available at:
#  http://github.com/Falcorian/Project-Euler-Solutions

""" The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

from time import time
from optparse import OptionParser
from math import floor,sqrt

# Optparse setup
usage = "usage: %prog"
parser = OptionParser(usage=usage)

(options, args) = parser.parse_args()

# Functions
def is_prime(num):
    """ Is a number prime? Returns bool. """
    if num < 2 or int(num) != float(num): # 0,1, negative numbers, and floats are not prime
        return False
    elif num < 4:
        return True # 2,3 are prime, others already excluded
    elif not num%2:
        return False
    elif num < 9: # We have now excluded 4,6,8
        return True
    elif not num%3:
        return False
    else:
        r = floor(sqrt(num))
        f = 5
        while f <= r:
            if not num%f:
                return False
            elif not num%(f+2):
                return False
            else:
                f += 6
        else:
            return True

def right_truncate(num):
    """ Right truncates a number:

    13 = right_truncate(137)

    """
    snum = str(num)
    newstr = snum[:-1]
    if newstr is '':
        return 0
    else:
        return int(newstr)

def left_truncate(num):
    """ Left truncates a number:

    37 = right_truncate(137)

    """
    snum = str(num)
    newstr = snum[1:]
    if newstr is '':
        return 0
    else:
        return int(newstr)

def is_left_prime(num):
    """ Returns True if a number is prime when truncated from the left side."""
    if not is_prime(num):
        return False
    # Test Left Truncating
    lnum = num
    while True:
        lnum = left_truncate(lnum)
        if not lnum: # 0
            break
        if not is_prime(lnum):
            return False

    # Passed our tests
    return True

def is_right_prime(num):
    """
    Returns True if a number is prime when truncated from the right side.
    """
    if not is_prime(num):
        return False
    # Test Left Truncating
    rnum = num
    while True:
        rnum = right_truncate(rnum)
        if not rnum: # 0
            break
        if not is_prime(rnum):
            return False

    # Passed our tests
    return True

# Constants
starts = ('2','3','5','7') # Only possible starts are 1 digit primes
addons = ('1','3','7','9') # Anything even is divisible by 2, 5 is divisible by 5, 0 by both.

# Solution
s = time()

# Right/Left Truncatable Primes (RTP/LTP) are a proper superset of Truncatable
# Primes (TP).  The union of RTP and LTP is equal to TP.  The size of RTP is
# much smaller than LTP, so we calculate that first, and then find the union
# with LTP

# Generate right truncatable primes
rights = list(starts[:])
rstack = list(starts[:])
while rstack:
    base = rstack.pop()
    for n in addons:
        num = int(base+n)
        if is_right_prime(num):
            rights.append(str(num))
            rstack.append(str(num))

# Find the members of right that are also left prime
twoprimes = [int(i) for i in rights if (is_left_prime(int(i)) and i not in starts)]

print sum(twoprimes),'in',time()-s,'secs'
