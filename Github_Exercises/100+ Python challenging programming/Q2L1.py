def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
         
    return result

print(factorial(8))

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# 
# print(fact(8))