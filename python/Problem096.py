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
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import time
from optparse import OptionParser
"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

puzzle:   003020600900305001001806400008102900700000008006708200002609500800203009005010300
solution: 483921657967345821251876493548132976729564138136798245372689514814253769695417382

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
# Optparse setup
usage = "usage: %prog [OPTIONS] -n number -b"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", action="store", type="string", dest="inFile", default=None, help="Input file containing Sudoku puzzles")
parser.add_option("-s", "--string", action="store", type="string", dest="inStr", default=None, help="Reads in a string of the Sudoku puzzle")

(options, args) = parser.parse_args()

# Functions
def combine(A,B):
    """ Returns a list of all posible combinations of a+b for a in A and b in B """
    return [a+b for a in A for b in B]

# Constants


# Classes
class sudoku:
    """ Stores a sudoku grid """
    def __init__(self,input):
        """ Initiates via an input string off the form A1A2A3... with 0 or . for blanks """
        self.input = input
        self.__init_vars() 
        self.__parse_input()

    def __init_vars(self):
        """ Initiates some data structures needed by the class.

            These could be hardcoded, but it is more compact to generate when needed."""
        self.rows   = ('A','B','C','D','E','F','G','H','I')
        self.cols   = ('1','2','3','4','5','6','7','8','9')
        self.nums   = self.cols
        self.cells  = combine(self.rows,self.cols)
        self.cells.sort()
        self.groups = ([combine(self.rows,c) for c in self.cols] + # Columns
                       [combine(r,self.cols) for r in self.rows] + # Rows
                       [combine(r,c)
                           for r in [('A','B','C'),('D','E','F'),('G','H','I')] 
                           for c in [('1','2','3'),('4','5','6'),('7','8','9')] 
                       ])                                          # Blocks

        # Need to clean this up
        self.connections = {}
        for cell in self.cells:
            cellList = []
            for group in self.groups:
                if cell in group:
                    cellList += group
            cellSet = set(cellList) - set(cell)
            cellSet.remove(cell)
            cellList = list(cellSet)
            cellList.sort()
            self.connections[cell] = tuple(cellList)

    def __parse_input(self):
        """ Reads in a gameboard as a string """
        self.grid = dict((self.cells[i],self.input[i]) for i in xrange(len(self.cells)))

    def __str__(self):
        """ Output the self.grid in human readable form """
        col_b = 3
        row_b = 3
        outStr = ""
        for row in self.rows:
            if row in ('D','G'):
                outStr += "------+-------+------\n"
            for col in self.cols:
                if col in ('4','7'):
                    outStr += "| "
                outStr += self.grid[row+col]+" "
                if col == '9':
                    outStr += ("\n" if row not in 'I' else '')
        return outStr

# Solution
p1 = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
if __name__ == '__main__':
    s = time.time()

    puzzle = sudoku(p1)
    print puzzle

    print time.time()-s,'secs'
