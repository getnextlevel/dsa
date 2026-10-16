import pytest

from longest_substr_chars import longest_substring


def test_happy_path():
    assert longest_substring("abcabcbb") == 3


def test_len_check():
    assert longest_substring("a") == 1


def test_empty_string():
    assert longest_substring("") == 0


def test_same_chars():
    assert longest_substring("aaaaaa") == 1


@pytest.mark.parametrize("s, expected", [
    ("pwwkew", 3),
    ("dvdf", 3),
    ("abba", 2),
    ("tmmzuxt", 5),
    ("abcdef", 6),
    ("aA", 2),
])
def test_longest_subst(s, expected):
    assert longest_substring(s) == expected
