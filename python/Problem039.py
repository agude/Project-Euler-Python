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
#  The most recent version of this program is available at:
#  http://github.com/Falcorian/Project-Euler-Solutions

""" If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?

"""

from time import time
from optparse import OptionParser
from math import sqrt

# Optparse setup
usage = "usage: %prog [OPTIONS] -n MAX"
parser = OptionParser(usage=usage)
parser.add_option("-n", action="store", type="int", dest="MAX", default=1000, help="find the perimeter that maximizes number of right triangles up to MAX")

(options, args) = parser.parse_args()

# Constants
MAX = options.MAX

# Solution
s = time()

# We note that are three cases:
#  a even, b even -> c even -> p even
#  a odd,  b odd  -> c even -> p even
#  a even, b odd  -> c odd  -> p even
#
# So we need only check even parameters
# We further note that the triangle inequality holds:
# a + b > c --> a + b + c > 2c --> p > 2c --> p/2 > c
# c > a or b, hence p / 2 > c,a,b

finalp = 0
finalcombo = 0
for p in xrange(12,MAX+1,2): # 12 is smallest perimeter
    combo = 0
    for a in xrange(1,p/2):
        bmax = p - a
        for b in xrange(a,bmax):
            c = sqrt(a*a+b*b)
            if int(c) == float(c) and a+b+c == p:
                combo += 1
    if combo > finalcombo:
        finalp = p
        finalcombo = combo

print finalp,'in',time()-s,'secs'