from collections import Counter

def longest_substring(s):
    counter = Counter()

    ans = left = 0

    for right in range(len(s)):
        counter[s[right]] += 1

        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    s = "abcabcbb"
    print(longest_substring(s))
