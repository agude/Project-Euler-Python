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

import time
from optparse import OptionParser
from decimal import getcontext,Decimal
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="max", default=1000, help="find the longest cycle of 1/d for d less than or equal to MAX")

(options, args) = parser.parse_args()

# Constants
getcontext().prec = 100
max = options.max

# Functions
def getCycleEvent(num,v=False):
    """
    Finds the length of a repeating cycle.
    """
    num = str(num)
    # Test for decimal
    try:
        if not num[1] == '.':
            if v: print "Not a Decimal"
            return 0
    except IndexError:
        if v: print "Number too short pre truncation"
        return 0
    # Find period using Floyd's cycle-finding algorithm
    ## Matching points
    num = num[2:] # Trimming off '0.'
    end = len(num)-1
    t = 0
    h = 1
    if t >= end or h >= end: # No cycles
        if v: print "Number too short post truncation"
        return 0
    tort = num[t]
    hare = num[h]

    while tort != hare:
        # End of array testing, dumby loop
        for z in xrange(2):
            h += 1 
            if h == end:
                if v: print "Hare ran off array while looking for matching points"
                return 0
        t += 1
        tort = num[t]
        hare = num[h]
    ## Finding the start, which is where they intersect again
    mu = 0
    t = 0
    tort = num[t]
    hare = num[h]
    while tort != hare:
        h += 1 
        if h == end:
            if v: print "Hare ran off array while looking for start"
            return 0
        t += 1
        tort = num[t]
        hare = num[h]
        mu += 1
    ## Find the period
    lam = 1
    h = t # Restart hare at start of array with tort
    hare = num[h]
    while tort != hare:
        h += 1 
        if h == end:
            if v: print "Hare ran off array while looking for period"
            return 0
        lam += 1

    return lam

# Solution
s = time.time()

for i in range(1,max):
    num = Decimal(1)/Decimal(i)
    print num,
    if getCycleEvent(num,v=True): print "\n"
print 'in',time.time()-s,'secs'
