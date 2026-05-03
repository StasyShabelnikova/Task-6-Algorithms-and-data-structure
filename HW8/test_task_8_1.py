from task_8_1 import max_subarray_sum


def test_basic_case():
    assert max_subarray_sum([1, 2, 3, 4, 5], 2) == 9


def test_k_equals_one():
    assert max_subarray_sum([3, 8, 1, 5], 1) == 8


def test_k_equals_len_array():
    assert max_subarray_sum([1, 2, 3], 3) == 6


def test_negative_numbers():
    assert max_subarray_sum([-5, -2, -7, -1], 2) == -7


def test_mixed_numbers():
    assert max_subarray_sum([3, -1, 4, -2, 5], 3) == 7


def test_empty_array():
    assert max_subarray_sum([], 2) is None


def test_k_bigger_than_array():
    assert max_subarray_sum([1, 2], 3) is None


def test_invalid_k():
    assert max_subarray_sum([1, 2, 3], 0) is None