# def fibonacci(n):
#     a, b = 0, 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#
# fibonacci_series = []
# for i in range(20):
#     fibonacci_series.append(fibonacci(i))
#
# n = 4
# count = 0
# arr = list(map(int, '1 1 1 1'.split()))
# for x in arr:
#     if x in fibonacci_series:
#         count += 1
# print(count)
#
import math


def is_Perfect_Square(K):
    s = int(math.sqrt(K))
    return s * s == K


def is_Fibonacci(R):
    return is_Perfect_Square(5 * R * R + 4) or is_Perfect_Square(5 * R * R - 4)


n = 4
count = 0
arr = list(map(int, '1 1 1 1'.split()))
for x in arr:
    if is_Fibonacci(x):
        count += 1
print(count)
