#!/usr/bin/env python

import pytest
import euler.graphs as eu


@pytest.fixture(scope="function")
def pyramid():
    tup = ((3,), (7, 4), (2, 4, 6), (8, 5, 9, 3))
    string = "3\n7 4\n2 4 6\n8 5 9 3"
    pg = eu.PyramidGraph(tup)

    return (pg, 23, tup, string)


def test_largest_sum(pyramid):
    graph = pyramid[0]
    largest_sum = pyramid[1]
    assert graph.largest_sum() == largest_sum


def test_getitem(pyramid):
    graph = pyramid[0]
    tup = pyramid[2]
    for i in range(len(tup)):
        assert graph[i] == tup[i]


def test_len(pyramid):
    graph = pyramid[0]
    tup = pyramid[2]
    assert len(graph) == len(tup)


def test_repr(pyramid):
    graph = pyramid[0]
    tup = pyramid[2]
    assert repr(graph) == repr(tup)


def test_str(pyramid):
    graph = pyramid[0]
    string = pyramid[3]
    assert str(graph) == string


@pytest.fixture(scope="function")
def vertex():
    v = eu.Vertex(0)

    return v


def test_vertex_add_and_remove_edge(vertex):
    e = eu.Edge(eu.Vertex(1), vertex)
    # Test adding
    vertex.add_edge(e)
    assert e in vertex.edges
    # Test removal
    vertex.remove_edge(e)
    assert e not in vertex.edges


def test_vertex_add_edges(vertex):
    edges = set((
        eu.Edge(eu.Vertex(1), vertex),
        eu.Edge(eu.Vertex(2), vertex),
    ))
    # Test adding
    vertex.add_edges(edges)
    for e in edges:
        assert e in vertex.edges


def test_vertex_has_incoming(vertex):
    # No incoming edges yet
    assert not vertex.has_incoming()
    # Add an incoming edge
    incoming = eu.Edge(eu.Vertex(1), vertex)
    vertex.add_edge(incoming)
    assert vertex.has_incoming()


def test_vertex_has_outgoing(vertex):
    # No incoming edges yet
    assert not vertex.has_outgoing()
    # Add an incoming edge
    outgoing = eu.Edge(vertex, eu.Vertex(0))
    vertex.add_edge(outgoing)
    assert vertex.has_outgoing()


def test_vertex_iter(vertex):
    edges = set((
        eu.Edge(eu.Vertex(1), vertex),
        eu.Edge(eu.Vertex(2), vertex),
    ))

    vertex.add_edges(edges)
    seen = 0
    for e in vertex:
        seen += 1
        assert e in edges
    assert seen == len(edges)


def test_vertex_str(vertex):
    assert str(vertex) == str(vertex.number)


def test_vertex_repr(vertex):
    assert repr(vertex) == repr(vertex.number)


def test_vertex_compare(vertex):
    vl = eu.Vertex(-1)
    vh = eu.Vertex(1)
    ve = eu.Vertex(0)
    assert vl < vertex < vh
    assert vh > vertex > vl
    assert ve == vertex


@pytest.fixture(scope="function")
def unweighted_edge():
    v0 = eu.Vertex(0)
    v1 = eu.Vertex(1)

    e = eu.Edge(v0, v1)

    return e, v0, v1


def test_edge_constructor(unweighted_edge):
    _, v0, v1 = unweighted_edge
    edges = (
        (v0, v1, False, 1),
        (v0, v1, False, 2),
        (v0, v1, True, 1),
        (v0, v1, True, 2),
    )
    for args in edges:
        e = eu.Edge(*args)
        v0 = args[0]
        v1 = args[1]
        assert e.tail == v0
        assert e.head == v1
        assert e.directed == args[2]
        assert e.weight == args[3]


def test_edge_other_vertex(unweighted_edge):
    _, v0, v1 = unweighted_edge
    edges = (
        (v0, v1, False, 1),
        (v0, v1, False, 2),
        (v0, v1, True, 1),
        (v0, v1, True, 2),
    )
    for args in edges:
        e = eu.Edge(*args)
        v0 = args[0]
        v1 = args[1]
        assert e.other_vertex(v0.number) == v1
        assert e.other_vertex(v1.number) == v0


def test_edge_str(unweighted_edge):
    e, v0, v1 = unweighted_edge
    # Unweighted
    assert str(e) == "0--(1)--1"
    # Weighted
    e.weight = 2
    assert str(e) == "0--(2)--1"
    # Directed Weighted
    e.directed = True
    assert str(e) == "0--(2)->1"
    # Directed Unweighted
    e.weight = 1
    assert str(e) == "0--(1)->1"


@pytest.fixture(scope="function")
def graph():
    g = eu.Graph()

    return g


def test_graph_add_vertex(graph):
    vert_num = 0
    graph.add_vertex(vert_num)
    assert len(graph.vertices) == 1
    assert graph.vertices[vert_num]


def test_graph_add_edge_no_exist(graph):
    graph.add_edge(0, 1)
    assert len(graph.vertices) == 2
    assert graph.vertices[0]
    assert graph.vertices[1]


def test_graph_add_edge_one_exist(graph):
    graph.add_vertex(0)
    assert graph.vertices[0]

    graph.add_edge(0, 1)
    assert len(graph.vertices) == 2
    assert graph.vertices[1]
    assert len(graph.edges) == 1


def test_graph_add_edge_two_exist(graph):
    graph.add_vertex(0)
    graph.add_vertex(1)
    assert graph.vertices[0]
    assert graph.vertices[1]

    graph.add_edge(0, 1)
    assert len(graph.vertices) == 2
    assert len(graph.edges) == 1


def test_graph_add_edge_loop(graph):
    graph.add_edge(0, 0)
    assert graph.vertices[0]
    assert len(graph.vertices) == 1
    assert len(graph.edges) == 1


def test_graph_iter(graph):
    graph.add_edge(0, 0)
    graph.add_edge(0, 1)
    seen = 0
    for edge in graph:
        assert edge in graph.edges
        seen += 1
    assert len(graph.edges) == seen


def test_graph_get_item(graph):
    for i in range(10):
        graph.add_vertex(i)
        assert graph[i] == graph.vertices[i]


def test_graph_len(graph):
    for i in range(10):
        graph.add_vertex(i)
        assert len(graph) == len(graph.vertices) == i+1
