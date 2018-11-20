#!/usr/bin/env python3

#  Copyright (C) 2017  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
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
#  The most recent version of this program is available at:
#  https://github.com/agude/Project-Euler

"""
A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.
"""

from euler.converter import iterable_to_int
from euler.graphs import Graph
from time import time


# Sorted and duplicates removed
CODES = (
    [1, 2, 9], [1, 6, 0], [1, 6, 2], [1, 6, 8], [1, 8, 0], [2, 8, 9],
    [2, 9, 0], [3, 1, 6], [3, 1, 8], [3, 1, 9], [3, 6, 2], [3, 6, 8],
    [3, 8, 0], [3, 8, 9], [6, 2, 0], [6, 2, 9], [6, 8, 0], [6, 8, 9],
    [6, 9, 0], [7, 1, 0], [7, 1, 6], [7, 1, 8], [7, 1, 9], [7, 2, 0],
    [7, 2, 8], [7, 2, 9], [7, 3, 1], [7, 3, 6], [7, 6, 0], [7, 6, 2],
    [7, 6, 9], [7, 9, 0], [8, 9, 0],
)


def problem_079(codes=CODES):
    start_time = time()

    # If the successful logins form a DAG, then we can sort them topologically
    # to get the answer.

    # Add all the successful logins to a graph
    graph = Graph()
    for code in CODES:
        for i in (0, 1):
            graph.add_edge(code[i], code[i+1], directed=True)

    # Topological sort
    sorted_vertices = []
    source_vertices = [v for _, v in graph.vertices.items() if not v.has_incoming()]
    while source_vertices:
        vert = source_vertices.pop()
        sorted_vertices.append(vert)

        # Remove all it's outgoing edges
        for outgoing_edge in vert.outgoing_edges():
            head = outgoing_edge.head
            tail = outgoing_edge.tail
            head.remove_edge(outgoing_edge)
            tail.remove_edge(outgoing_edge)

        # Look for new "source" vertices
        for _, v in graph.vertices.items():
            if v not in sorted_vertices and not v.has_incoming():
                source_vertices.append(v)

    answer = iterable_to_int(sorted_vertices)

    end_time = time() - start_time

    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':

    problem_079(CODES)
