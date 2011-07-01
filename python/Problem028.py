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
parser.add_option("-n", "--number", action="store", type="int", dest="num", default=1001, help="find the sum of the diagonals of a num x num spiral")

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
        # No center is defined if even.
        assert n%2!= 0
        self.size = n
        self.b = None
        self.__makeBoard()
        self.sum = None
        self.__sumDiags()

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
        i = n/2
        j = n/2
        self.b[i][j] = m
        if n < 3:
            return
        while True:
            # Fill Right
            if i == -1 or j == -1:
                break
            else:
                i,j = self.__fillHori(i,j,Right=True)
            # Fill Down
            if i == -1 or j == -1:
                break
            else:
                i,j = self.__fillVert(i,j,Down=True)
            # Fill Left
            if i == -1 or j == -1:
                break
            else:
                i,j = self.__fillHori(i,j,Left=True)
            # Fill Up
            if i == -1 or j == -1:
                break
            else:
                i,j = self.__fillVert(i,j,Up=True)

    def __fillHori(self,i,j,Left=True,Right=False):
        """
        Fills the board to the left/(right) as long as values exist in the row above/(below).
        """
        # You may only set one option
        if Right:
            Left = False
            dir = +1
        if Left:
            Right = False
            dir = -1
        # Initial Value
        m = self.b[i][j]
        # Fill until no matching above/below
        while True:
            m += 1
            j += dir
            try:
                if self.b[i+dir][j] != False:
                    self.b[i][j] = m
                else:
                    break
            except IndexError:
                return -1,-1
        # Fill one more
        try:
            self.b[i][j] = m
        except IndexError:
            return -1,-1
        m += 1

        return i,j

    def __fillVert(self,i,j,Up=True,Down=False):
        """
        Fills the board to up/(down) as follows as long as values exist in the column to the right/(left).
        """
        # You may only set one option
        if Down:
            Up = False
            dir = -1
        if Up:
            Down = False
            dir = +1
        # Initial value
        m = self.b[i][j]
        # Fill until no matching to the right/left
        while True:
            m += 1
            i -= dir
            try:
                if self.b[i][j+dir] != False:
                    self.b[i][j] = m
                else:
                    break
            except IndexError:
                return -1,-1
        # Fill one more
        try:
            self.b[i][j] = m
        except IndexError:
            return -1,-1
        m += 1

        return i,j

    def __sumDiags(self):
        """
        Returns the sum of numbers on the diagonal
        """
        self.sum = 0
        for i in range(self.size):
            self.sum += self.b[i][i]
            if i != self.size - i - 1: # Don't double count middle
                self.sum += self.b[self.size - i - 1][i]

    def __str__(self):
        """
        Format for printing.
        """
        outStr = '\n'
        width = len(str((self.size * self.size))) + 1
        for i in range(self.size):
            for j in range(self.size):
                outStr += str(self.b[i][j]).center(width,' ')
            outStr += '\n'

        return outStr

# Solution
s = time()
sp = spiral(options.num)
print sp.sum,'in',time()-s,'secs'
