"""
Given an array a[ ] of N elements. Consider array as a circular array i.e.
element after an is a1. The task is to find maximum sum of the absolute difference
between consecutive elements with rearrangement of array elements allowed i.e. after
any rearrangement of array elements find |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1|.
"""


def maxSum(arr, n):
    arr.sort()
    s = 0
    i = 0
    j = n-1
    while i < j:
        s += abs(arr[i] - arr[j])
        s += abs(arr[i+1] - arr[j])
        i += 1
        j -= 1
    s += abs(arr[0] - arr[i])
    return s

#     answer = [0] * n
#     arr.sort()
#     i = j = 0
#     while j < n-1:
#         print(answer)
#         answer[j], answer[j+1] = arr[i], arr[n-i-1]
#         i += 1
#         j += 2
#     if n % 2 != 0:
#         answer[j] = arr[i]
#     print(answer)
#     s = 0
#     for i in range(n-1):
#         s += abs(answer[i] - answer[i+1])
#     s += abs(answer[0] - answer[-1])
#     return s


N = 4
a = [4, 2, 1, 8]
print(maxSum(a, N))
