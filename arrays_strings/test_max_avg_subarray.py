import pytest

from max_avg_subarray import max_sub_average

def test_example():
    assert max_sub_average([1,12,-5,-6,50,3], 4) == 12.75

def test_another_example():
    assert max_sub_average([5], 1) == 5.000

def test_empty_nums():
    with pytest.raises(ValueError):
        max_sub_average([], 2)

def test_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        max_sub_average([1,2], 0)