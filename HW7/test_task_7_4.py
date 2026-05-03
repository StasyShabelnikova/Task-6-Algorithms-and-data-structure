from task_7_4 import is_bipartite


def test_empty_graph():
    assert is_bipartite({}) is True


def test_single_vertex():
    graph = {1: []}
    assert is_bipartite(graph) is True


def test_simple_bipartite_graph():
    graph = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 4],
        4: [1, 3]
    }
    assert is_bipartite(graph) is True


def test_not_bipartite_triangle():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert is_bipartite(graph) is False


def test_disconnected_bipartite_graph():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert is_bipartite(graph) is True


def test_disconnected_with_bad_component():
    graph = {
        1: [2],
        2: [1],
        3: [4, 5],
        4: [3, 5],
        5: [3, 4]
    }
    assert is_bipartite(graph) is False


def test_self_loop():
    graph = {
        1: [1]
    }
    assert is_bipartite(graph) is False