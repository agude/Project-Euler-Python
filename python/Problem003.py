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
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 317584931803?
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="number", default=317584931803, help="finds the largest prime factor of this number")

(options, args) = parser.parse_args()

# Solution
s = time.time()

number = options.number
x = 2
primes = []

while number > 1:
    if number%x == 0:
        primes.append(x)        
        number = number/x
    x += 1

print max(primes),'in',time.time()-s,'secs' 