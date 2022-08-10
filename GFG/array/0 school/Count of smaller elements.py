"""
Given a sorted array A of size N. Find number of elements which are less than or equal to given element X.
"""


def countOfElements(a, n, x):
    count = 0
    for item in a:
        if item <= x:
            count += 1
    return count


A = [1, 2, 4, 5, 8, 10]
N = 6
K = 9
print(countOfElements(A, N, K))
