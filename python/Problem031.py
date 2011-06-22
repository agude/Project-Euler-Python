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
from numpy import array, ceil, floor, sqrt, bool, nonzero, ones, int64
"""
In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).

It is possible to make $2 in the following way:

    1$1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
    
How many different ways can $2 be made using any number of coins?
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="max", default=200, help="find number of ways to make MAX pence with British coins")

(options, args) = parser.parse_args()

# Constants
max = options.max

# Solution
## First we find the maximum of each type
s = time.time()
max1 = max
max2 = (max/2) + 1
max5 = (max/5) + 1
max10 = (max/10) + 1
max20 = (max/20) + 1
max50 = (max/50) + 1
max100 = (max/100) + 1
max200 = (max/200) + 1

## Then we loop over possible combinations
combos = 0
for ones in xrange(0,max1+1):
    amount = ones
    if amount > max:
        break
    for twos in xrange(0,max2+1):
        amount = ones + 2*twos
        if amount > max:
            break
        for fives in xrange(0,max5+1):
            amount = ones + 2*twos + 5*fives
            if amount > max:
                break
            for tens in xrange(0,max10+1):
                amount = ones + 2*twos + 5*fives + 10*tens
                if amount > max:
                    break
                for twents in xrange(0,max20+1):
                    amount = ones + 2*twos + 5*fives + 10*tens + 20*twents
                    if amount > max:
                        break
                    for fifts in xrange(0,max50+1):
                        amount = ones + 2*twos + 5*fives + 10*tens + 20*twents + 50*fifts
                        if amount > max:
                            break
                        for hunds in xrange(0,max100+1):
                            amount = ones + 2*twos + 5*fives + 10*tens + 20*twents + 50*fifts + 100*hunds
                            if amount > max:
                                break
                            for twohunds in xrange(0,max200+1):
                                amount = ones + 2*twos + 5*fives + 10*tens + 20*twents + 50*fifts + 100*hunds + 200*twohunds
                                if amount == max:
                                    combos += 1
                                    #print "GOOD:",ones,twos,fives,tens,twents,fifts,hunds,twohunds

print combos,'in',time.time()-s,'secs'
