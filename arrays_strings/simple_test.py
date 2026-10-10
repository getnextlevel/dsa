
def calc_factorial(num):
    ans = 1
    for i in range(num, 0, -1):
        ans = ans * i
    return ans

print(calc_factorial(5))
