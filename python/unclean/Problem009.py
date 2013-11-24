#  Copyright (C) 2011  Alexander Gude -
#  alex.public.account+ProjectEulerSolutions@gmail.com
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

from time import time
from optparse import OptionParser

""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n NUM"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--num", action="store", type="int", dest="NUM", default=1000, help="find a,b,c such that a**2+b**2 == c**2 and a+b+c == NUM")

(options, args) = parser.parse_args()

# Constants
NUM = options.NUM

# Solution
s = time()

run = True
for c in range(NUM-3,1,-1):
    for b in range(NUM-c-1,1,-1):
        a = NUM - b - c
        if not a < b < c or a < 0:
            continue
        elif a**2 + b**2 == c**2:
            run = False
            break
    if not run:
        break

print a*b*c,'in',time()-s,'secs'
