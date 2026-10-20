"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

"""

def equal_contiguous_array(nums):
    counts = {0: -1}

    ans = count = 0

    for idx, num in enumerate(nums):
        count += 1 if num == 1 else -1

        if count in counts:
            ans = max(ans, idx - counts[count])
        else:
            counts[count] = idx

    return ans

if __name__ == "__main__":
    nums = [0,1]

    print(equal_contiguous_array(nums))