"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

def product_except_self(nums):
    length = len(nums)
    L = [0] * length
    R = [0] * length
    ans = [0] * length


    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i-1] * L[i-1]


    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        R[i] = nums[i+1] * R[i+1]
    

    for i in range(length):
        ans[i] = L[i] * R[i]

    return ans


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(product_except_self(nums))