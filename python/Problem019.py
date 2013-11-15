#  Copyright (C) 2013  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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

"""
You are given the following information, but you may prefer to do some research
for yourself.

* 1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight,
rain or shine.
And on leap years, twenty-nine.

*A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
"""

from time import time
from optparse import OptionParser
from datetime import date

# Optparse setup
usage = "usage: %prog [OPTIONS]"
parser = OptionParser(usage=usage)
parser.add_option("-s", action="store", type="int", dest="START_YEAR", default=1901, help="start counting Sundays from the start of this year")
parser.add_option("-e", action="store", type="int", dest="END_YEAR", default=2000, help="stop counting Sundays at the end of this year")

(options, args) = parser.parse_args()

# Solution
start_time = time()

total = 0

for year in range(options.START_YEAR, options.END_YEAR + 1):
    for month in range(1, 13):
        if (date(year, month, 1).weekday() is 6):
            total += 1

end_time = time() - start_time

print(total, 'in', end_time, 'secs')
