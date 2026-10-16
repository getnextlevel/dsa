import pytest

from count_jewels import numJewelsInStones


def test_happy_path1():
    jewels = "aA"
    stones = "aAAbbbb"

    assert numJewelsInStones(jewels, stones) == 3


def test_happy_path2():
    jewels = "z"
    stones = "ZZ"

    assert numJewelsInStones(jewels, stones) == 0


def test_value_error():
    jewels = "z"
    stones = "ZZ"
    with pytest.raises(ValueError):
        numJewelsInStones(stones, jewels)

