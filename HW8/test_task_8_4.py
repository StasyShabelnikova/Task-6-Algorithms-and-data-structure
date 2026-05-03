from task_8_4 import find_pivot_index


def test_rotated_array():
    assert find_pivot_index([4, 5, 6, 7, 1, 2, 3]) == 4


def test_not_rotated_array():
    assert find_pivot_index([1, 2, 3, 4, 5]) == 0


def test_two_elements_rotated():
    assert find_pivot_index([2, 1]) == 1


def test_two_elements_not_rotated():
    assert find_pivot_index([1, 2]) == 0


def test_single_element():
    assert find_pivot_index([10]) == 0


def test_empty_array():
    assert find_pivot_index([]) == -1


def test_rotated_near_end():
    assert find_pivot_index([3, 4, 5, 6, 1, 2]) == 4


def test_rotated_near_start():
    assert find_pivot_index([5, 1, 2, 3, 4]) == 1