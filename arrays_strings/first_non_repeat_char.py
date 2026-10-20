"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

"""
from collections import Counter

def first_unique_char(s):
    counter = Counter(s)

    for idx, char in enumerate(s):
        if counter[char] == 1:
            return idx
        
    return -1


if __name__ == "__main__":
    s = "leetcode"
    print(first_unique_char(s))