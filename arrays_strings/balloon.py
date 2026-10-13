"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1

"""

"""

counter = {b: 1, a: 1, l: 1, o: 1, n: 1}

len: 5
b, a, n : 1
o, l: 1 * 2

{b: 1, a: 1, l: 2, o: 2, n: 1} -> set = 1, 2. --> true --> occurrence -> 1
{b: 2, a: 2, l: 4, o: 4, n: 2} --> set = 2, 4. --> true --> occurrence -> 2

Optimized approach

We will use bitwise operator '>>' here. Which mean x >> y ==> x // 2 ^ y, floor division, because l and o appears twice the number of other chars.

Floor division will be by 2 ^ 1, in this case since l and o appears twice more than the other chars.

We will take the minimum occurrence of these characters.


"""

from collections import Counter

def count_balloons(text):
    counter = Counter(text)

    return min(counter['b'], counter['a'], counter['l'] >> 1, counter['o'] >> 1, counter['n'])


if __name__ == "__main__":
    text = "nlaebolko"

    print(count_balloons(text))


