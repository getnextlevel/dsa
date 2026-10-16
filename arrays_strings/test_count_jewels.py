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


def test_jewels_longer_than_stones_raises():
    with pytest.raises(ValueError):
        numJewelsInStones("abc", "a")


def test_jewels_same_length_as_stones():
    assert numJewelsInStones("ab", "ab") == 2


def test_stones_exactly_50_chars():
    assert numJewelsInStones("a", "a" * 50) == 50


def test_stones_over_50_chars():
    with pytest.raises(ValueError):
        numJewelsInStones("a", "a" * 51)


def test_no_jewels_in_stones():
    assert numJewelsInStones("xyz", "abc") == 0


def test_all_stones_are_jewels():
    assert numJewelsInStones("abc", "cabcab") == 6


def test_repeated_stones_counted_each_time():
    assert numJewelsInStones("a", "aaaa") == 4


def test_case_sensitive():
    assert numJewelsInStones("a", "A") == 0


def test_single_char_each():
    assert numJewelsInStones("a", "a") == 1


def test_empty_jewels():
    assert numJewelsInStones("", "abc") == 0


def test_empty_stones():
    assert numJewelsInStones("a", "") == 0


def test_both_empty():
    assert numJewelsInStones("", "") == 0


def test_duplicate_jewels():
    assert numJewelsInStones("aa", "aab") == 2

