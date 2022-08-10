"""
Given a sorted array Arr of size N and a value X, find the number of array
elements less than or equal to X and elements more than or equal to X.
"""


def getMoreAndLess(arr, n, x):
    out = [0, 0]
    for item in arr:
        if item >= x:
            out[1] += 1
        if item <= x:
            out[0] += 1
    return out


A = [1, 2, 8, 10, 11, 12, 19]
N = 7
X = 0
print(getMoreAndLess(A, N, X))
