from task_6_3 import coin_change


def test_basic():
    assert coin_change([1, 2, 5], 11) == 3


def test_impossible():
    assert coin_change([2], 3) == -1


def test_zero_amount():
    assert coin_change([1, 2, 5], 0) == 0


def test_one_coin():
    assert coin_change([5], 10) == 2


def test_no_solution():
    assert coin_change([4, 6], 7) == -1


def test_minimum_choice():
    assert coin_change([1, 3, 4], 6) == 2