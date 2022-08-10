"""
Given an array of N distinct elements, the task is to find all elements
in array except two greatest elements in sorted order.
"""


def findElements(a, n):
    a.sort()
    return a[:n-2]


A = [7, -2, 3, 4, 9, -1]
N = 6
print(*findElements(A, N))
