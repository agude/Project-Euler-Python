#  Copyright (C) 2010  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="max", default=20, help="answer must be divisible by 1,2,3,...,number")

(options, args) = parser.parse_args()

# Solution
s = time.time()

max = options.max

i=0
while True:
    i += (max*(max-1)) # We know the number has to be divisible by max, and max-1, so we incriment by this number
    for j in range(3,max-1): # Now we check all numbers from max-2 to 3, 2 is free if 4 is, and 1 is useless
        if i%j:
            break
        else:
            continue
    else: # This statement only exicutes if the for loops runs through all i%j without breaking, i.e. we have our number
        print i,'in',time.time()-s,'secs'
        exit()