from task_6_1 import max_sequence
import pytest

def test_from_vk():
    assert max_sequence([3, 2, 8, 9, 5, 10]) == 3

def test_from_vk_1():
    assert max_sequence([1, 2, 7, 9, 0, 10]) == 4

def test_from_vk_2():
    assert max_sequence([8, 8, 8, 8]) == 1

def test_zero():
    assert max_sequence([]) == 0

def test_biggger():
    assert max_sequence([2, 3, 4, 1, 3, 5, 6, 7]) == 5 

def test_alone():
    assert max_sequence([3]) == 1

def test_all():
    assert max_sequence([1, 3, 6, 8, 9]) == 5

def test_repeat():
    assert max_sequence([1, 2, 2, 3]) == 2

def test_negative():
    assert max_sequence([-2, 3, -4, 9, 10, 11]) == 4