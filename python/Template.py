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

from time import time
from optparse import OptionParser
"""
"""
# Optparse setup
usage = "usage: %prog [OPTIONS]"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--num", action="store", type="int", dest="num", default=0, help="")

(options, args) = parser.parse_args()

# Classes

# Functions

# Constants

# Solution
s = time()

print 'in',time()-s,'secs'
