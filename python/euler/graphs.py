class PyramidGraph:
    """ An object that stores a Pyramid shaped graph with numbers at each
    vertex and edges connecting each number with the two below it.

    For example, in the following pyramid, the 3 in row 0 connects to the 7 in
    row 2 and the 4 in row 2. The 4 in row 2 connects to the 4 in row 3 and the
    6 in row 3, and so on.

           3
          7 4
         2 4 6
        8 5 9 3
    """
    def __init__(self, input_tuple):
        """ Initialize pyramid graph from a nested list.

        The input list should contain a collection of lists of numbers. The
        first sublist should have size 1, the second size 2, and so on. For
        example:

        ((3,), (7, 4), (2, 4, 6), (8, 5, 9, 3))

        This input would represent the pyramid:

           3
          7 4
         2 4 6
        8 5 9 3

        Args:
            input_tuple (list of lists of numbers): A nested set of lists of
                numbers.

        Raises:
            ValueError: If the sublists in input_tuple do not have size 1, 2,
                3, ..., n
        """
        tempory_list = []
        assert_size = 1
        # We store the pyramid as a tuple, regardless of the form of the input
        for sublist in input_tuple:
            # The first sublist must have length 1, the second length 2, etc.
            if assert_size != len(sublist):
                raise ValueError("Input tuple does not contain a pyramid")
            assert_size += 1
            tempory_list.append(tuple(sublist))
        self.__internal_tuple = tuple(tempory_list)

    def largest_sum(self):
        """ Return the largest sum possible from traversing the pyramid from
        top to bottom.

        We search from the bottom, and when every two "paths" meet we only keep
        the larger one.

        Raises:
           TypeError: If the elements of the tuple do not support addition, or
               if they are unorderable.
        """
        # Starting at the bottom, get all the rows in pairs (n, n-1), (n-1,
        # n-2), ..., all the way to (1, 0), with 0 as the top
        bottom_sums = list(self[-1])
        for top_row_id in range(-2, -len(self) - 1, -1):
            top_sums = list(self[top_row_id])
            for i in range(len(top_sums)):
                top_sums[i] += max(bottom_sums[i], bottom_sums[i + 1])
            bottom_sums = top_sums

        return top_sums[0]

    def __getitem__(self, key):
        """ Return rows from the pyramid. """
        return self.__internal_tuple.__getitem__(key)

    def __len__(self):
        """ Return the number of levels in the pyramid. """
        return self.__internal_tuple.__len__()

    def __repr__(self):
        """ Returns an object that could be used to create a new graph.
        """
        return self.__internal_tuple.__repr__()

    def __str__(self):
        """ Returns a human readable version of the graph. """
        lines = []
        for sublist in self.__internal_tuple:
            str_sublist = (str(i) for i in sublist)
            lines.append(" ".join(str_sublist))
        return "\n".join(lines)
