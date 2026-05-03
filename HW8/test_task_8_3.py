from task_8_3 import find_max_length


def test_basic_case():
    assert find_max_length([0, 1, 0, 0, 1]) == 4


def test_simple_pair():
    assert find_max_length([0, 1]) == 2


def test_no_equal_count():
    assert find_max_length([0, 0, 0]) == 0


def test_all_equal_full_array():
    assert find_max_length([0, 1, 1, 0]) == 4


def test_longest_in_middle():
    assert find_max_length([0, 0, 1, 0, 1, 1, 1]) == 6


def test_empty_array():
    assert find_max_length([]) == 0


def test_only_ones():
    assert find_max_length([1, 1, 1, 1]) == 0


def test_complex_case():
    assert find_max_length([1, 0, 1, 1, 0, 0, 1]) == 6