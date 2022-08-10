"""
Given an array Arr of size N, print second largest element from an array.
"""


def print2largest(arr, n):
    arr = list(set(arr))
    arr.sort(reverse=True)
    return arr[1]


A = [12, 35, 35, 1, 10, 34, 1]
N = 6
print(print2largest(A, N))
