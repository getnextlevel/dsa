import pytest

from two_sum import find_two_sum


def test_happy_path():
    assert find_two_sum([2,7,11,15], 9) == [0, 1]

def test_happy_path1():
    assert find_two_sum([3, 2, 4], 6) == [1, 2]