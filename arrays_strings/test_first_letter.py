import pytest

from first_letter_appear_twice import get_first_letter, get_first_letter_using_set


def test_happy_path():
    assert get_first_letter('abccbaacz"') == 'c'

def test_happy_path1():
    assert get_first_letter('abcdd') == 'd'


def test_happy_path3():
    assert get_first_letter_using_set('abccbaacz"') == 'c'

def test_happy_path4():
    assert get_first_letter_using_set('abcdd') == 'd'