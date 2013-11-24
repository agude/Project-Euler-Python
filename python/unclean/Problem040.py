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

""" An irrational decimal fraction is created by concatenating the positive
integers:

0.12345678910 >1< 112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 *  d10 *  d100 * d1000 *  d10000 * d100000 * d1000000

"""

from time import time
from optparse import OptionParser

# Optparse setup
usage = "usage: %prog [OPTIONS]"
parser = OptionParser(usage=usage)

(options, args) = parser.parse_args()

# Solution
s = time()

## Generate string
i=1
num = '0.'
while True:
    num += str(i)
    if len(num) > 1000000 + 1:
        break
    i += 1

## Add up digits
finalsum = int(num[1+1]) * int(num[10+1]) * int(num[100+1]) * int(num[1000+1]) * int(num[10000+1]) * int(num[100000+1]) * int(num[1000000+1])

print finalsum,'in',time()-s,'secs' 
