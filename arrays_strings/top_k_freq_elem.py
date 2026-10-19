"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

"""

from collections import Counter

def most_freq_elements_top_k(nums, k):
    counter = Counter(nums)

    sorted_counter = dict(sorted(counter.items(), key= lambda item: item[1], reverse=True))
    print("sorted counter : ", sorted_counter)

    return list(sorted_counter.keys())[:k]


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(most_freq_elements_top_k(nums, k))