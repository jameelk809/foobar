"""
Given two arrays of equal size N and an integer K. The task is to check
if after permuting both arrays, we get sum of their corresponding element
greater than or equal to k i.e. Ai + Bi >= K for all i (from 0 to N-1).
Return true if possible, else false.
"""


def isPossible(a, b, n, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        if a[i] + b[i] < k:
            return False
    return True


a = [2, 1, 3]
b = [7, 8, 9]
n = 3
k = 10
if isPossible(a, b, n, k):
    print(1)
else:
    print(0)
