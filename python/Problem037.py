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
#  The most recent version of this program is avaible at:
#  http://github.com/Falcorian/Project-Euler-Solutions

import time
from optparse import OptionParser
from math import floor,sqrt
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
# Optparse setup
usage = "usage: %prog"
parser = OptionParser(usage=usage)

(options, args) = parser.parse_args()

# Functions
def isPrime(num):
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

def rightTruncate(num):
    """
    Right truncates a number:

    13 = rightTruncate(137)
    """
    snum = str(num)
    newstr = snum[:-1]
    if newstr is '':
        return 0
    else:
        return int(newstr)

def leftTruncate(num):
    """
    Left truncates a number:

    37 = rightTruncate(137)
    """
    snum = str(num)
    newstr = snum[1:]
    if newstr is '':
        return 0
    else:
        return int(newstr)

def isLeftPrime(num):
    """
    Returns True if a number is prime when truncated from the left side.
    """
    if not isPrime(num):
        return False
    # Test Left Truncating
    lnum = num
    while True:
        lnum = leftTruncate(lnum)
        if not lnum: # 0
            break
        if not isPrime(lnum):
            return False

    # Passed our tests
    return True

def isRightPrime(num):
    """
    Returns True if a number is prime when truncated from the right side.
    """
    if not isPrime(num):
        return False
    # Test Left Truncating
    rnum = num
    while True:
        rnum = rightTruncate(rnum)
        if not rnum: # 0
            break
        if not isPrime(rnum):
            return False

    # Passed our tests
    return True

def isTwoSidePrime(num):
    """
    Returns True if a number is prime when truncated from both sides.
    """
    if not isPrime(num):
        return False
    # Test Right Truncating
    rnum = num
    while True:
        rnum = rightTruncate(rnum)
        if not rnum: # 0
            break
        if not isPrime(rnum):
            return False
    # Test Left Truncating
    lnum = num
    while True:
        lnum = leftTruncate(lnum)
        if not lnum: # 0
            break
        if not isPrime(lnum):
            return False

    # Passed our tests
    return True

# Constants
starts = ('2','3','5','7')
addons = starts + ('1','4','6','8','9')
rights = []

# Solution
s = time.time()

# Generate right truncatable primes
rights = list(starts[:])
rstack = list(starts[:])
while rstack:
    base = rstack.pop()
    for n in addons:
        num = int(base+n)
        if isRightPrime(num):
            rights.append(str(num))
            rstack.append(str(num))
print len(rights)
del rstack

# Generate left truncatable primes
lefts = list(starts[:])
lstack = list(starts[:])
while lstack:
    base = lstack.pop()
    for n in addons:
        num = int(n+base)
        if isLeftPrime(num):
            lefts.append(str(num))
            lstack.append(str(num))

print len(lefts)
del lstack
from sys import exit
exit()

print 'in',time.time()-s,'secs'
