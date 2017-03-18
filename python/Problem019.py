#!/usr/bin/env python3

#  Copyright (C) 2014  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
#  https://github.com/agude/Project-Euler

"""
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight,
rain or shine.
And on leap years, twenty-nine.

* A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
"""


def problem_019(start_year=1901, end_year=2000):
    from datetime import date
    from time import time

    # Constant
    SUNDAY = 6

    # Solution
    start_time = time()

    # We simply loop over all the firsts of the month and check if they are
    # Sunday (using datatime, which does all the hard work for us, but then,
    # why wouldn't we take advatnage of it?)
    answer = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if date(year, month, 1).weekday() is SUNDAY:
                answer += 1

    end_time = time() - start_time
    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':
    from optparse import OptionParser

    # Optparse setup
    usage = "usage: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option("-s", action="store", type="int", dest="START_YEAR", default=1901, help="start counting Sundays from the start of this year")
    parser.add_option("-e", action="store", type="int", dest="END_YEAR", default=2000, help="stop counting Sundays at the end of this year")

    (options, args) = parser.parse_args()

    # Constants
    START_YEAR = options.START_YEAR
    END_YEAR = options.END_YEAR

    problem_019(START_YEAR, END_YEAR)
