"""
You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).
"""


def printAl(arr, n):
    for i in range(0, n, 2):
        print(arr[i], end=' ')


n = 5
arr = [1, 2, 3, 4, 5]
printAl(arr, n)
