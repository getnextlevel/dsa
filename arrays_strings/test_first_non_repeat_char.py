import pytest

from first_non_repeat_char import first_unique_char


@pytest.mark.parametrize("s, expected", [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("", -1)
])
def test_cases(s, expected):
    assert first_unique_char(s) == expected


