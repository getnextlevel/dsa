import pytest

from k_radius_subarray import k_radius_subarray


def test_example():
    assert k_radius_subarray([7,4,3,9,1,8,5,2,6], 3) == [-1,-1,-1,5,4,4,-1,-1,-1]