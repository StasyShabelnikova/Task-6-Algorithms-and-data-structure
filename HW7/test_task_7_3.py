import pytest
from task_7_3 import dijkstra


def test_single_vertex():
    graph = {
        'A': {}
    }
    result = dijkstra(graph, 'A')
    assert result == {'A': 0}


def test_simple_graph():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2},
        'C': {'A': 4, 'B': 2}
    }
    result = dijkstra(graph, 'A')
    assert result == {
        'A': 0,
        'B': 1,
        'C': 3
    }


def test_chain_graph():
    graph = {
        'A': {'B': 2},
        'B': {'A': 2, 'C': 3},
        'C': {'B': 3}
    }
    result = dijkstra(graph, 'A')
    assert result == {
        'A': 0,
        'B': 2,
        'C': 5
    }


def test_disconnected_graph():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {}
    }
    result = dijkstra(graph, 'A')
    assert result == {
        'A': 0,
        'B': 1,
        'C': float("inf")
    }


def test_multiple_paths():
    graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 5, 'B': 1}
    }
    result = dijkstra(graph, 'A')
    assert result == {
        'A': 0,
        'B': 1,
        'C': 2
    }


def test_zero_weight_edges():
    graph = {
        'A': {'B': 0},
        'B': {'A': 0, 'C': 2},
        'C': {'B': 2}
    }
    result = dijkstra(graph, 'A')
    assert result == {
        'A': 0,
        'B': 0,
        'C': 2
    }