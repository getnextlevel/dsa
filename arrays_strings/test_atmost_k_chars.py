import pytest

from atmost_k_chars import find_longest_substring


def test_example():
    assert find_longest_substring("eceba", 2) == 3

def test_another_example():
    assert find_longest_substring("aa", 1) == 2

def test_k_larger_than_distinct_chars():
    assert find_longest_substring("abc", 10) == 3

def test_k_equals_one():
    assert find_longest_substring("aabbbc", 1) == 3

def test_all_same_chars():
    assert find_longest_substring("aaaaa", 2) == 5

def test_all_distinct_chars():
    assert find_longest_substring("abcdef", 3) == 3

def test_longest_at_end():
    assert find_longest_substring("abcddddd", 2) == 6

def test_single_char():
    assert find_longest_substring("a", 1) == 1

def test_empty_string():
    assert find_longest_substring("", 2) == 0

def test_k_zero():
    assert find_longest_substring("abc", 0) == 0
