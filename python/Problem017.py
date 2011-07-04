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

from time import time
from optparse import OptionParser
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000, help="find the number of letters to write the first NUM numbers")

(options, args) = parser.parse_args()

# Functions
def get_char_len(num):
    """ Returns the number of English letters used to write out the number

    """
    snum = repr(num)
    try:
        one = int(snum[-1])
    except IndexError:
        one = 0
    try: 
        ten = int(snum[-2])
    except IndexError:
        ten = 0
    try:
        hun = int(snum[-3])
    except IndexError:
        hun = 0
    try:
        tho = int(snum[-4])
    except IndexError:
        tho = 0

    string = thos[tho]
    if string and hun != 0:
        string += ' and '
    string += huns[hun]
    if string and ( ten != 0 or one != 0):
        string += ' and '
    if ten != 1:
        string += tens[ten] + ones[one]
    else:
        string += teens[one]
        
    #print num,string.replace(' ','')

    return len(string.replace(' ',''))

# Constants
ones={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:''}
teens={1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen',0:'ten'}
tens={1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:''}
huns={1:'one hundred',2:'two hundred',3:'three hundred',4:'four hundred',5:'five hundred',6:'six hundred',7:'seven hundred',8:'eight hundred',9:'nine hundred',0:''}
thos={1:'one thousand',0:''}

# Solution
s = time()

count=0
for num in xrange(1,options.num+1):
    count += get_char_len(num)

print count,'in',time()-s,'secs'
