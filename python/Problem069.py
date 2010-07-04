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
from math import sqrt
from optparse import OptionParser
"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.

n   Relatively Prime    phi(n)    n/phi(n)
2   1                   1         2
3   1,2                 2         1.5
4   1,3                 2         2
5   1,2,3,4             4         1.25
6   1,5                 2         3
7   1,2,3,4,5,6         6         1.1666...
8   1,3,5,7             4         2
9   1,2,4,5,7,8         6         1.5
10  1,3,7,9             4         2.5

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000000, help="find the last ten digits of the sum n**n")

(options, args) = parser.parse_args()

# Solution
s = time.time()

def fattorizza(n):
    c = 0
    f = {}
    for i in xrange(2, int(sqrt(n))):
        if not n%i:
            f[i] = 1
            n /= i
        while not n%i:
            f[i] += 1
            vn = n
            n /= i
        if n == 1:
            return f
    f[n] = 1
    return f
 
maxnum = 0
maxi   = 0

def fi(n):
    if n == 1:
        return 1
    fi = 1
    f = fattorizza(n)
    for p in f:
        k = f[p]
        fi *= (p-1)*p**(k-1)
    return fi

for i in range(1,options.num+1):
    num = float(i)/float(fi(i))
    if num > maxnum:
        maxnum = num
        maxi   = i

print maxi,'in',time.time()-s,'secs'
