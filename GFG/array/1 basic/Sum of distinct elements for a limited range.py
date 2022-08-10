"""
Given an array, arr[] of N elements such that every element of the array
is an integer in the range 1 to n, the task is to find the sum of all the
distinct elements of the array.
"""


def sumOfDistinct(arr, n):
    return sum(set(arr))
#     s = 0
#     dup = []
#     for num in arr:
#         if num not in dup:
#             dup.append(num)
#             s += num
#     return s



N = 9
A = [5, 1, 2, 4, 6, 7, 3, 6, 7]
# A = [1,2,1,1,2,3]
print(sumOfDistinct(A, N))
