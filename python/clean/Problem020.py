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

""" 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

"""

from time import time
from optparse import OptionParser

# Optparse setup
usage = "usage: %prog [OPTIONS] -n NUM"
parser = OptionParser(usage=usage)
parser.add_option("-n", action="store", type="int", dest="NUM", default=100, help="find the sum of the digits of NUM")

(options, args) = parser.parse_args()

# Constants
NUM = options.NUM

# Solution
s = time()

finalnum = 1
for j in xrange(1,NUM+1):
    finalnum *= j

strnum = str(finalnum)

total = 0
for i in range(len(strnum)):
    term = strnum[i]
    if term == 'L':
        continue
    else:
        total += int(term)

print total,'in',time()-s,'secs'
