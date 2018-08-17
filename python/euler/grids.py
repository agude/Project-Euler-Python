from itertools import chain
import euler.countable as countable


class Grid(object):
    """ An object that stores a grid of numbers.

    For example:

        08 02 22 97
        49 49 99 40
        81 49 31 73
    """

    def __init__(self, grid):
        """ Initialize the grid from a list of strings.

        The input list should be of the form:

            [ '1 2 3', '4, 5, 6']

        Which represents a grid like:

            1 2 3
            4 5 6

        Args:
            grid (list of strings): A list of strings containing space
                separated numbers.

        Raises:
            ValueError: If the number of numbers per row is not constant.
            ValueError: If part of the string does not convert via `float()`.
        """
        # Convert the strings into rows of floats
        self.rows = []
        row_len = None
        for row in grid:
            row = [float(num) for num in row.split()]
            if row_len is None:
                row_len = len(row)
            else:
                if len(row) != row_len:
                    raise ValueError("each row must have the same number of numbers")

            self.rows.append(row)

        # Break the grid into other useful representations
        self.__make_columns()
        self.__make_backward_diagonals()
        self.__make_forward_diagonals()

    def __make_columns(self):
        """ Fills in self.cols """
        self.cols = []
        for i in range(len(self.rows[0])):
            col = []
            for row in self.rows:
                col.append(row[i])
            self.cols.append(col)

    def __make_diagonals(self, rows):
        """ Make diagonals from a list of rows. """
        output = []
        n_col = len(rows[0])  # Number of columns
        n_row = len(rows)     # Number of rows

        for diff in range(-n_col+1, n_row):
            dia = []
            for i in range(n_row):
                j = i-diff
                if i >= 0 and n_col - 1 >= j >= 0:
                    dia.append(rows[i][j])
            output.append(dia)

        return output

    def __make_backward_diagonals(self):
        """ Fills in self.backward_diagonals, that is the diagonals like: \\\\\\ """
        self.backward_diagonals = self.__make_diagonals(self.rows)

    def __make_forward_diagonals(self):
        """ Fills in self.forward_diagonals, that is the diagonals like: ////// """
        # Make a reversed row
        rrows = [r[::-1] for r in self.rows]
        self.forward_diagonals = self.__make_diagonals(rrows)

    def max_product(self, n):
        """ Returns the max product of n numbers from within the grid.

        For example, for the grid (with n=2):

        1 2
        3 4

        It would look at all products (1*2, 1*3, 1*4, 3*2, 3*4) and
        return the max 12.

        Combinations that are two short (for example, the diagonal
        (3,) or (2,), are ignored.

        Args:
            n (int): The number of numbers from the grid to take a
                product with.

        Returns:
            int: The maximum product.

        Raises:
            ValueError: if n is non-positive.
        """
        # Check that the input if valid
        if not countable.is_positive_integer(n):
            print(n)
            raise ValueError("n is a not a positive integer")
        # Otherwise try all products and keep the max
        max_product = float("-inf")
        chained = chain(
            self.rows,
            self.cols,
            self.backward_diagonals,
            self.forward_diagonals,
        )
        for row in chained:
            # If the row is too short, ignore it
            if len(row) < n:
                continue
            # Compute the product, and save if it is larger than the
            # previous max
            for i in range(len(row) - n + 1):
                product = 1
                to_check = row[i:i+n]
                for number in to_check:
                    product *= number
                max_product = max(product, max_product)

        return max_product
