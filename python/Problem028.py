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

import time
from optparse import OptionParser
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number"
parser = OptionParser(usage=usage)
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1000, help="find the number of letters to write the first NUM numbers")

(options, args) = parser.parse_args()

# Class
class spiral:
    """
    Class to store and manipulate spiral.
    """
    def __init__(self,n):
        """ 
        Size is n x n block. n must be odd.
        """
        n = int(n)
        assert n%2!= 0
        self.size = n
        self.__makeBoard()

    def __makeBoard(self):
        """
        Creates a blank board and fills it with numbers
        """
        # Makes a blank board
        n = self.size
        self.b = []
        for i in range(n):
            self.b.append([])
            for j in range(n):
                self.b[i].append(False)

        # Fills it
        m = 1
        s_i = n/2
        s_j = n/2
        self.b[s_i][s_j] = m
        if n < 3:
            return
        i,j,m = self.__fillHori(s_i,s_j,Right=True)

    def __fillHori(self,i,j,Left=True,Right=False):
        """
        Fills the board to the left as follows as long as values exist in the row above.
        """
        if Right:
            Left = False
            dir = +1
        if Left:
            Right = False
            dir = -1

        m = self.b[i][j]
        # Fill until no matching above
        while True:
            m += 1
            j += dir
            if self.b[i+dir][j] != False:
                try:
                    self.b[i][j] = m
                except IndexError:
                    return -1,-1
            else:
                break
        # Fill one more
        try:
            self.b[i][j] = m
        except IndexError:
            return -1,-1
        m += 1

        if Right:
            return self.__fillVert(i,j,Down=True)
        if Left:
            return self.__fillVert(i,j,Up=True)

    def __fillVert(self,i,j,Up=True,Down=False):
        """
        Fills the board to the left as follows as long as values exist in the row above.
        """
        if Down:
            Up = False
            dir = +1
        if Up:
            Down = False
            dir = -1
        m = self.b[i][j]
        # Fill until no matching above
        while True:
            m += 1
            i += dir
            if self.b[i+dir][j] != False:
                print "True"
                try:
                    self.b[i][j] = m
                except IndexError:
                    return -1,-1
            else:
                break
        # Fill one more
        try:
            self.b[i][j] = m
        except IndexError:
            return -1,-1
        m += 1

        print self.__str__()
        if Up:
            return self.__fillHori(i,j,Right=True)
        if Down:
            return self.__fillHori(i,j,Left=True)

    def __str__(self):
        """
        Format for printing.
        """
        outStr = ''
        width = len(str((self.size * self.size))) + 2
        for i in range(self.size):
            for j in range(self.size):
                outStr += str(self.b[i][j]).center(width,' ')
            outStr += '\n'

        return outStr

# Constants

# Solution
s = time.time()

sp = spiral(5)
print sp

print 'in',time.time()-s,'secs'
