#  Copyright (C) 2011  Alexander Gude - alex.public.account+PySudokuSolver@gmail.com
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
rows   = ('A','B','C','D','E','F','G','H','I')
cols   = ('1','2','3','4','5','6','7','8','9')
nums   = ('1','2','3','4','5','6','7','8','9')
cells  = combine(rows,cols)
groups = (
          [combine(rows,c) for c in cols] + # Columns
          [combine(r,cols) for r in rows] + # Rows
          [combine(r,c)
           for r in [('A','B','C'),('D','E','F'),('G','H','I')] 
           for c in [('1','2','3'),('4','5','6'),('7','8','9')] 
          ]                                 # Blocks
         )

connections = {}
for cell in cells:
    cellList = []
    for group in groups:
        if cell in group:
            cellList += group
    cellSet = set(cellList)
    cellSet.remove(cell)
    cellList = list(cellSet)
    cellList.sort()
    connections[cell] = tuple(cellList)

# Solution
if __name__ == '__main__':
    s = time.time()

    print time.time()-s,'secs'
