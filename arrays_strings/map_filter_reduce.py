"""
map(func, iterable)
filter(func, iterable)
reduce(func, iterable)

lambda --> single use function and for single line functions

"""

def get_square(num):
    return num * num



numbers = [1, 2, 3, 4, 5]

normal_way_squared = map(get_square, numbers)

squared = map(lambda x: x * x, numbers)

print(list(normal_way_squared))
print(list(squared))

even_nums = filter(lambda x: x % 2 == 0, numbers)

print(list(even_nums))

from functools import reduce


all_mults = reduce(lambda x, y: x * y, numbers)

print(all_mults)