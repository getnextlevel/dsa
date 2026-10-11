"""
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

We have to implement sliding window and hash concept here together, ask why? because we need to have a count of distinct characters.

So we maintain 2 counters left and right for the sliding window.

length of substring is right - left + 1

Also, if the count of a character in hash, becomes 0 we delete it from it.


"""

from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)

    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1

        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del(counts[s[left]])
            left += 1
        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    s = "eceba"
    k = 2

    print(find_longest_substring(s, k))