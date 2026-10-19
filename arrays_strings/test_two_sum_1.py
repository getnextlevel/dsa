import pytest

from two_sum_1 import get_two_sum


def test_happy_path():
    assert get_two_sum([2,7,11,15], 9) == [1, 0]


def test_same_element_not_reused():
    assert sorted(get_two_sum([3,2,4], 6)) == [1, 2]


def test_negative_numbers():
    assert sorted(get_two_sum([-3,4,3,90], 0)) == [0, 2]


def test_invalid_target():
    with pytest.raises(ValueError("Target cannot be 0")):
        get_two_sum([1,2,3], 0)