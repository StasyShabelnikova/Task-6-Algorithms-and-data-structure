import pytest
from task_7_1 import has_cycle


def test_empty_graph():
    graph = {}
    assert has_cycle(graph) == False


def test_single_vertex():
    graph = {1: []}
    assert has_cycle(graph) == False


def test_no_cycle_simple_chain():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2]
    }
    assert has_cycle(graph) == False


def test_simple_cycle_triangle():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert has_cycle(graph) == True


def test_cycle_in_component():
    graph = {
        1: [2],
        2: [1],

        3: [4, 5],
        4: [3, 5],
        5: [3, 4]
    }
    assert has_cycle(graph) == True


def test_disconnected_no_cycle():
    graph = {
        1: [2],
        2: [1],

        3: [4],
        4: [3]
    }
    assert has_cycle(graph) == False


def test_self_loop():
    graph = {
        1: [1]
    }
    assert has_cycle(graph) == True


def test_complex_graph():
    graph = {
        1: [2],
        2: [1, 3, 4],
        3: [2, 4],
        4: [2, 3]
    }
    assert has_cycle(graph) == True


