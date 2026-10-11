"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
"""

def get_first_letter(s):
    hash_map = {}

    for char in s:
        if char not in hash_map:
            hash_map[char] = 1
        elif char in hash_map and hash_map[char] == 1:
            return char
        else:
            hash_map[char] += 1
        # print("hash_map: ", hash_map)


def get_first_letter_using_set(s):
    """
    In this function we will use set.
    We will maintain a set and keep adding the elements as we iterate over s.
    With each iteration we will check if the character is in the set 
    which means, the character has appeared more than once and we will stop the loop there itself.
    """

    seen = set()
    
    for char in s:
        if char in seen:
            return char
        seen.add(char)


if __name__ == "__main__":
    s = "abccbaacz"
    print(get_first_letter(s))

    print(get_first_letter_using_set(s))
