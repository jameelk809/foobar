"""
Given an unsorted array Arr[] of N integers and a Key which is present in this array.
You need to write a program to find the start index( index where the element is
first found from left in the array ) and end index( index where the element is first
found from right in the array ).
"""


def findIndex(a, N, key):
    out = []
    for i in range(N):
        if a[i] == key:
            out.append(i)
    if len(out) == 0:
        return [-1, -1]
    return [out[0], out[-1]]


A = [23, 29, 30, 21, 16, 10, 29, 27, 19, 12, 30, 20, 10, 27, 30, 24, 20, 27, 22, 16, 27, 24, 24, 11, 12, 29]
N = 26
key = 29
print(findIndex(A, N, key))


