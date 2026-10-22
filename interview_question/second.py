"""

Fibonacci series: 0, 1, 1, 2, 3, 5, 8, ....

input - int 
"""

# def get_fibo(num):
#     if num == 0 or num == 1:
#         return num
#     # result = 1
#     # print(result)
#     output = [0] * num
#     output[0], output[1] = 0, 1
#     for i in range(2, num):
#         output[i] = output[i - 1] + output[i-2]
#     # print("output : ", output)
#     return output


# if __name__ == "__main__":
#     print(get_fibo(8))


"""

a = [1, 2, 3]
b = a
c = b

 --> loc00001 --< a, b, c

print(sys.getrefcount(a)) ## mem reference count
--> 3
 
del b

--> loc00001 --< a, c

print(sys.getrefcount(a)) 

--> 2
 
c.append(4)
--> loc00001 --< [1, 2, 3, 4] --< a, c
 
print(a)  

--> [1, 2, 3, 4]
 
del a
---> deletes the reference of a 
---> loc00001 --< c
 
print(c)   
--> loc00001 --< [1, 2, 3, 4]


"""
import sys

def verify_ref_call():
    a = [1, 2, 3]
    b = a
    c = b

    print(sys.getrefcount(a)) 

    del b

    print(sys.getrefcount(a)) 

    c.append(4)

    print(a)

    del a

    print(c)


if __name__ == "__main__":
    verify_ref_call()