import sys

"""
Given an array arr of size N with all initial values as 0, the task is to perform
the following M range increment operations as shown below:
Increment(ai, bi, ki) : Increment values from index 'ai' to 'bi' by 'ki'.
After M operations, calculate the maximum value in the array arr[].
"""


def findMax(n, m, a, b, c):
    """---------------time limit exceeded----------------"""
    # arr = [0]*n
    # for i in range(m):
    #     for j in range(a[i], b[i]+1, 1):
    #         arr[j] += c[i]
    #     print(arr)
    # return max(arr)

    # correct
    arr = [0 for i in range(n + 1)]
    for i in range(m):
        lowerbound = a[i]
        upperbound = b[i]
        arr[lowerbound] += c[i]
        arr[upperbound + 1] -= c[i]
    sum = 0
    res = -1 - sys.maxsize
    for i in range(n):
        sum += arr[i]
        res = max(res, sum)
    return res


N = 4
M = 3
A = [1, 0, 3]
B = [2, 0, 3]
K = [603, 286, 882]
# N = 5
# A = [0, 1, 2]
# B = [1, 4, 3]
# K = [100, 100, 100]
# M = 3
print(findMax(N, M, A, B, K))
