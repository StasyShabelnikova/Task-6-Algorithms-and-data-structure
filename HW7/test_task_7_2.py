import pytest
from task_7_2 import is_tree


def test_empty_graph():
    graph = {}
    assert is_tree(graph) is True


def test_single_vertex():
    graph = {1: []}
    assert is_tree(graph) is True


def test_simple_tree():
    graph = {
        1: [2, 3],
        2: [1],
        3: [1]
    }
    assert is_tree(graph) is True


def test_chain_tree():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3]
    }
    assert is_tree(graph) is True


def test_graph_with_cycle():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert is_tree(graph) is False


def test_disconnected_graph():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert is_tree(graph) is False


def test_disconnected_with_cycle():
    graph = {
        1: [2],
        2: [1],
        3: [4, 5],
        4: [3, 5],
        5: [3, 4]
    }
    assert is_tree(graph) is False


def test_self_loop():
    graph = {
        1: [1]
    }
    assert is_tree(graph) is False