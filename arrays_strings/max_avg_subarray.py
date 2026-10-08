"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

"""


def max_sub_average(nums, k):

    if len(nums) == 0:
        raise ValueError("Empty nums")
    
    if k < 1:
        raise ZeroDivisionError("Cannot divide by less than 1")
    

    ans = sum(nums[:4])
    curr = ans

    for right in range(k, len(nums), 1):
        curr += nums[right] - nums[right - k]
        ans = max(ans, curr)

    return ans / k

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print("hi")
    print("helo ", max_sub_average(nums, k))
