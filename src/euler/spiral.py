from typing import List, Tuple


class Spiral:
    """
    Class to store and manipulate a number spiral.
    """
    def __init__(self, n: int) -> None:
        """
        Size is n x n block. n must be odd.
        """
        n = int(n)
        # No center is defined if even, so can not continue
        if n % 2 == 0:
            raise ValueError("spiral can not have even size")

        self.size: int = n
        self.b: List[List[int]] = []
        self.__makeBoard()
        self.sum: int = 0
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
        m: int = 1
        i: int = n//2
        j: int = n//2
        self.b[i][j] = m
        if n < 3:
            return
        while True:
            # Fill Right
            if i == -1 or j == -1:
                break
            else:
                i, j = self.__fillHori(i, j, Right=True)
            # Fill Down
            if i == -1 or j == -1:
                break
            else:
                i, j = self.__fillVert(i, j, Down=True)
            # Fill Left
            if i == -1 or j == -1:
                break
            else:
                i, j = self.__fillHori(i, j, Left=True)
            # Fill Up
            if i == -1 or j == -1:
                break
            else:
                i, j = self.__fillVert(i, j, Up=True)

    def __fillHori(self, i: int, j: int, Left: bool=True, Right: bool=False) -> Tuple[int, int]:
        """
        Fills the board to the left/(right) as long as values exist in the row
        above/(below).
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
                if self.b[i+dir][j]:
                    self.b[i][j] = m
                else:
                    break
            except IndexError:
                return -1, -1
        # Fill one more
        try:
            self.b[i][j] = m
        except IndexError:
            return -1, -1
        m += 1

        return i, j

    def __fillVert(self, i: int, j: int, Up: bool=True, Down: bool=False) -> Tuple[int, int]:
        """
        Fills the board to up/(down) as follows as long as values exist in the
        column to the right/(left).
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
                if self.b[i][j+dir]:
                    self.b[i][j] = m
                else:
                    break
            except IndexError:
                return -1, -1
        # Fill one more
        try:
            self.b[i][j] = m
        except IndexError:
            return -1, -1
        m += 1

        return i, j

    def __sumDiags(self):
        """
        Returns the sum of numbers on the diagonal
        """
        self.sum = 0
        for i in range(self.size):
            self.sum += self.b[i][i]
            if i != self.size - i - 1:  # Don't double count middle
                self.sum += self.b[self.size - i - 1][i]

    def __str__(self) -> str:
        """
        Format for printing.
        """
        outStr: str = '\n'
        width = len(str((self.size * self.size))) + 1
        for i in range(self.size):
            for j in range(self.size):
                outStr += str(self.b[i][j]).center(width, ' ')
            outStr += '\n'

        return outStr
