from task_8_2 import subarray_sum


def test_basic_case():
    assert subarray_sum([3, 8, 6, 9, 2, 1, 4], 11) == 2


def test_simple_case():
    assert subarray_sum([1, 1, 1], 2) == 2


def test_with_negative_numbers():
    assert subarray_sum([1, -1, 0], 0) == 3


def test_no_subarray():
    assert subarray_sum([1, 2, 3], 7) == 0


def test_one_element_equals_k():
    assert subarray_sum([5], 5) == 1


def test_one_element_not_equals_k():
    assert subarray_sum([5], 3) == 0


def test_empty_array():
    assert subarray_sum([], 0) == 0


def test_all_zeroes():
    assert subarray_sum([0, 0, 0], 0) == 6