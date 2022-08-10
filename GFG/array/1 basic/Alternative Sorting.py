"""
Given an array arr[] of N distinct integers, output the array in such
a way that the first element is first maximum and the second element is
the first minimum, and so on.
"""


def alternateSort(arr, N):
    arr.sort()
    res = [0]*N
    i = j = 0
    while j < N-1:
        res[j], res[j+1] = arr[N-i-1], arr[i]
        i += 1
        j += 2
    if N % 2 != 0:
        res[j] = arr[i]
    return res


N = 7
A = [7, 1, 2, 3, 4, 5, 6]
print(alternateSort(A, N))
