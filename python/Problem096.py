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
        # MAY RUN FOREVER!
        while not self.__is_solved():
            for c in self.cells:
                self.__remove_solved(c)

    def __init_vars(self):
        """ Initiates some data structures needed by the class.

            These could be hardcoded, but it is more compact to generate when needed."""
        self.rows   = ('A','B','C','D','E','F','G','H','I')
        self.cols   = ('1','2','3','4','5','6','7','8','9')
        self.numl   = self.cols
        self.nums   = ''.join(self.cols)
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
        

    def __remove_solved(self,cell):
        """ For a cell, removes all values from its possible list that are already assigned else where """
        g   = self.grid
        con = self.connections[cell]
        sol = self.solved
        nl = self.numl

        if not sol[cell]:
            rl = [sol[c] for c in con if sol[c] in nl]
            for l in rl:
                g[cell] = g[cell].replace(l,'')

        if len(g[cell]) == 1:
            sol[cell] = g[cell]

    def __parse_input(self):
        """ Reads in a gameboard as a string """
        c  = self.cells
        p  = self.input 
        nl = self.numl
        ns = self.nums
        self.grid   = dict( (c[i],p[i]) if p[i] in nl else (c[i],ns) for i in range(len(c)) )
        self.solved = dict( (c[i],p[i]) if p[i] in nl else (c[i],False) for i in range(len(c)) )
        for cl in c:
            self.__remove_solved(cl)

    def __str__(self):
        """ Allows printing of self.grid in human readable form """
        g = self.grid
        outStr = ""
        width = max(len(g[i]) for i in g.keys())
        for row in self.rows:
            if row in ('D','G'):
                outStr += (("-"*(4+3*width) + "+")*3)[:-1] + "\n"
            for col in self.cols:
                if col in ('4','7'):
                    outStr += "| "
                elif col == '1':
                    outStr += " "
                cWidth = width-len(g[row+col])+1
                outStr += g[row+col]+" "*cWidth
                if col == '9':
                    outStr += ("\n" if row != 'I' else '')
        return outStr

    def __is_solved(self):
        """ Check to see if solved """
        for cell in self.solved:
            if not self.solved[cell]:
                return False
        return True

# Solution
p1 = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
if __name__ == '__main__':
    s = time.time()

    puzzle = sudoku(p1)
    print puzzle

    print 'Solved in',time.time()-s,'secs'
