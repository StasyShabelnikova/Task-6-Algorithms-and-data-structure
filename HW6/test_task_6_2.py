from task_6_2 import Pascal_triangle
import pytest

def test_zero():
    assert Pascal_triangle(0) == []

def test_one():
    assert Pascal_triangle(1) == [[1]]

def test_basic():
    assert Pascal_triangle(3) == [[1], [1,1], [1,2,1]]

def test_basic_1():
    assert Pascal_triangle(5) == [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

