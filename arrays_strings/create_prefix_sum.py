

nums = [1,12,-5,-6,50,3]

# prefix_sum = [1, 13, 8, 2, 52, 3]

prefix = [nums[0]]


for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])

print(prefix)
