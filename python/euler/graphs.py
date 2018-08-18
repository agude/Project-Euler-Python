from functools import total_ordering
from typing import Dict, List, Set, Tuple, Union
import collections


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
    def __init__(self, input_tuple) -> None:
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
        assert_size: int = 1
        # We store the pyramid as a tuple, regardless of the form of the input
        for sublist in input_tuple:
            # The first sublist must have length 1, the second length 2, etc.
            if assert_size != len(sublist):
                raise ValueError("Input tuple does not contain a pyramid")
            assert_size += 1
            tempory_list.append(tuple(sublist))
        self.__internal_tuple = tuple(tempory_list)

    def largest_sum(self) -> int:
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
        bottom_sums: List[int] = list(self[-1])
        for top_row_id in range(-2, -len(self) - 1, -1):
            top_sums: List[int] = list(self[top_row_id])
            for i in range(len(top_sums)):
                top_sums[i] += max(bottom_sums[i], bottom_sums[i + 1])
            bottom_sums = top_sums

        return top_sums[0]

    def __getitem__(self, key: int):
        """ Return rows from the pyramid. """
        return self.__internal_tuple.__getitem__(key)

    def __len__(self):
        """ Return the number of levels in the pyramid. """
        return self.__internal_tuple.__len__()

    def __repr__(self):
        """ Returns an object that could be used to create a new graph.
        """
        return self.__internal_tuple.__repr__()

    def __str__(self) -> str:
        """ Returns a human readable version of the graph. """
        lines = []
        for sublist in self.__internal_tuple:
            str_sublist = (str(i) for i in sublist)
            lines.append(" ".join(str_sublist))
        return "\n".join(lines)


@total_ordering
class Vertex:
    def __init__(self, number: int) -> None:
        self.number: int = number
        self.edges: Set[Edge] = set([])

    def add_edge(self, edge: "Edge"):
        """ Add an edge to the list of edges. """
        self.edges.add(edge)

    def add_edges(self, edges: Set["Edge"]):
        """ Add a list of edges to the list of edges. """
        self.edges.update(edges)

    def remove_edge(self, edge: "Edge"):
        """ Remove an edge from the list of edges. """
        if edge in self.edges:
            self.edges.remove(edge)

    def has_incoming(self) -> bool:
        """ Return true if any incoming edges, false otherwise. """
        for edge in self.edges:
            if edge.head.number == self.number:
                return True
        return False

    def has_outgoing(self) -> bool:
        """ Return true if any outgoing edges, false otherwise. """
        for edge in self.edges:
            if edge.tail.number == self.number:
                return True
        return False

    def outgoing_edges(self) -> Set["Edge"]:
        """ Return a list of vertices that have an incoming edge from this vertex. """
        edges: Set["Edge"] = set()
        for edge in self.edges:
            if edge.tail.number == self.number:
                edges.add(edge)
        return edges

    def __iter__(self):
        return self.edges.__iter__()

    def __str__(self):
        return self.number.__str__()

    def __repr__(self):
        return self.number.__repr__()

    def __lt__(self, other: "Vertex"):
        if self.__class__ is other.__class__:
            return self.number.__lt__(other.number)
        return NotImplemented

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.number.__eq__(other.number)
        return NotImplemented


Num = Union[int, float]


class Edge:
    def __init__(self, tail: Vertex, head: Vertex, directed: bool=False, weight: Num=1) -> None:
        self.head: Vertex = head
        self.tail: Vertex = tail
        self.directed: bool = directed
        self.weight: Num = weight

    def __str__(self) -> str:
        """ Allow printing. """
        mid = "--"
        if self.directed:
            mid = "->"
        out_str = "{tail}--({weight}){mid}{head}".format(
            tail=self.tail,
            weight=self.weight,
            mid=mid,
            head=self.head,
        )
        return out_str

    def other_vertex(self, vertex: Vertex) -> Vertex:
        """ Given the number of a vertex, returns the other vertex. That is, if
        given the head, returns the tail, and vica versa. """
        if vertex == self.head.number:
            return self.tail
        return self.head


class Graph:
    def __init__(self):
        self.vertices: Dict[int, Vertex] = {}
        self.edges: Set[Edge] = set()

    def add_vertex(self, number: int):
        v: Vertex = Vertex(number)
        self.vertices[number] = v

    def add_edge(self, tail: int, head: int, directed: bool=False, weight: Num=1):
        """ Creates a vertex between tail and head, and adds tail and head to
        the graph if they don't already exist.

        Args:
            tail: The number of a vertex.
            head: The number of a second vertex.
            directed: Bool indicating if the edge is directed.
            weight: A number indicating the edge weight.
        """
        # Try to get the tail from our list of vertices
        try:
            tail_v = self.vertices[tail]
        except KeyError:
            self.add_vertex(tail)
            tail_v = self.vertices[tail]
        # Try to get the head from our list of vertices
        try:
            head_v = self.vertices[head]
        except KeyError:
            self.add_vertex(head)
            head_v = self.vertices[head]
        # Make the edge
        new_edge = Edge(tail_v, head_v, directed, weight)
        self.edges.add(new_edge)
        # Add the edge to the vertices
        tail_v.add_edge(new_edge)
        head_v.add_edge(new_edge)

    def __iter__(self):
        return self.edges.__iter__()

    def __getitem__(self, key):
        return self.vertices.__getitem__(key)

    def __len__(self) -> int:
        return self.vertices.__len__()

    def __str__(self) -> str:
        out_str: str = ""
        keys: List[int] = sorted(self.vertices.keys())
        for key in keys:
            out_str += "Vertex " + str(key) + '\n'
            edge_strs: List[str] = []
            for edge in self[key]:
                edge_strs.append(str(edge))
            edge_strs.sort()
            for edge_str in edge_strs:
                out_str += '\t' + edge_str + '\n'

        return out_str
