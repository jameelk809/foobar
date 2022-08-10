"""
Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.
"""


def swapKth(arr, n, k):
    arr[k-1], arr[n-k] = arr[n-k], arr[k-1]


A = [1, 2, 3, 4, 5, 6, 7, 8]
N = 8
K = 3
swapKth(A, N, K)
print(A)
