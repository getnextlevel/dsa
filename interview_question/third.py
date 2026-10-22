"""
Given an array arr[] of non-negative integers and a 
value sum, the task is to check if there is a subset of 
the given array whose sum is equal to the given sum.

Examples:
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: True
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output : False



arr = [3, 34, 4, 12, 5, 2]

sorted_array = [2, 3, 4, 5, 12, 34]

left = right = 0

running_sum = 0

while right < len(arr):
    running_sum += arr[right]

    if running_sum == sum: Return true

    if running_sum < sum: right += 1
    else: left  


    
arr = [3, 34, 4, 12, 5, 2],
sorted_arr = [2, 3, 4, 5, 12, 34], sum = 30

"""


def get_subset_equals(arr, target):
    arr.sort()

    left = right = running_sum = 0

    while right < len(arr) and left < len(arr):
        running_sum += arr[right]

        if running_sum == target:
            return True
        elif running_sum < target:
            right += 1
        else:
            left += 1

    return False


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    target = 30
    print(get_subset_equals(arr, target))

    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    print(get_subset_equals(arr, target))