"""

Problem: Return the indices of the two numbers that add up to target.
Input: nums = [3, 2, 4], target = 6 → Expected output: [1, 2], because nums[1] + nums[2] = 2 + 4 = 6. (Not [0, 0]: you can't use the 3 twice.)

"""

def find_two_sum(nums: list, target: int) -> int:
    seen = {}
    
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        else:
            seen[x] = i
            
    return "Not Found"



if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(find_two_sum(nums, target))