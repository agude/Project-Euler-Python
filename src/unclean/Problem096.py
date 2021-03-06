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

from copy import deepcopy,copy
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
        self.__analytical_solve()

    def __analytical_solve(self):
        """ Solves the puzzle as far as possible without having to guess values """
        while not self.__is_solved():
            ucells = tuple( (c for c in self.solved.keys() if not self.solved[c]) )
            for c in ucells:
                self.__remove_solved(c)
                if len(self.grid[c]) > 1:
                    self.__update_constraints(c)
#            print self.__str__()

    def __init_vars(self):
        """ Initiates some data structures needed by the class.

            These could be hardcoded, but it is more compact to generate when needed."""
        self.rows   = ('A','B','C','D','E','F','G','H','I')
        self.cols   = ('1','2','3','4','5','6','7','8','9')
        self.numl   = self.cols
        self.nums   = ''.join(self.cols)
        self.cells  = combine(self.rows,self.cols)
        self.cells.sort()
        # Groups of cells (Rows, Columns, Blocks, and all)
        self.gcol   = [combine(self.rows,c) for c in self.cols]
        self.grow   = [combine(r,self.cols) for r in self.rows]
        self.gblk   = [combine(r,c)
                           for r in [('A','B','C'),('D','E','F'),('G','H','I')]
                           for c in [('1','2','3'),('4','5','6'),('7','8','9')]
                       ]
        self.groups = self.gcol + self.grow + self.gblk

        # Enumerate the different types of connections
        self.connections = {'all':{},'row':{},'col':{},'block':{}}
        for cell in self.cells:
            self.connections['all'][cell]   = set(chain.from_iterable([g for g in self.groups if cell in g])) - set([cell])
            self.connections['row'][cell]   = set(chain.from_iterable([g for g in self.grow   if cell in g])) - set([cell])
            self.connections['col'][cell]   = set(chain.from_iterable([g for g in self.gcol   if cell in g])) - set([cell])
            self.connections['block'][cell] = set(chain.from_iterable([g for g in self.gblk   if cell in g])) - set([cell])

    def __remove_solved(self,cell):
        """ For a cell, removes all values from its possible list that are already assigned else where """
        if not self.solved[cell]:
            rl = (self.solved[c] for c in self.connections['all'][cell] if (self.solved[c] in self.numl))
            for l in rl:
                self.grid[cell] = self.grid[cell].replace(l,'')

        if len(self.grid[cell]) == 1:
            self.solved[cell] = self.grid[cell]

    def __update_constraints(self,cell):
        """ Check to see if cell is contrained to be one value """
        for key in ('col','row','block'):
            group = self.connections[key][cell]
            possible = self.grid[cell]
            rm = ''.join((self.grid[c] for c in group))
            for l in rm:
                possible = possible.replace(l,'')
                if possible=='': 
                    break
                        
            if len(possible) == 1:
                self.grid[cell] = possible
                self.solved[cell] = possible
                return 0
            

    def __parse_input(self):
        """ Reads in a gameboard as a string """
        self.grid   = dict( (v,self.input[i]) if self.input[i] in self.numl else (v,self.nums) for i,v in enumerate(self.cells) )
        self.solved = dict( (v,self.input[i]) if self.input[i] in self.numl else (v,False) for i,v in enumerate(self.cells) )

    def return_output(self):
        """ Returns the solution as a string in the same form as the input """
        return ''.join( (self.solved[c] for c in self.cells) )

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
        return self.solved == self.grid

# Solution
p1  = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
p2  = ".8.9.3.4...61.7.....3...6..6...89..49.......37..64...2..9...3.....8.62...1.7.5.9."
p3  = "5...9..42...53.....1.2.....42....1.6..3...9..6.9....27.....2.9.....87...94..63..8"
p4  = "300010000000600490000458300080006210147285060026300070005134000031007000000060005"
p5  = "630000004001040030700000001903504120400903006067208903100000002050090600300000059"

if __name__ == '__main__':
    s = time()

    for i in range(1):
        s1 = sudoku(p2)
    
    print s1

    print 'Solved in',time()-s,'secs'
