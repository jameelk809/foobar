"""
Given an array of numbers forms 0 to 9 of size N. Your task is to rearrange
elements of the array such that after combining all the elements of the
array number formed is maximum.
"""


def MaxNumber(arr, n):
    out = ''
    arr.sort(reverse=True)
    for item in arr:
        out += str(item)
    return out


N = 5
A = [9, 0, 1, 3, 0]
print(MaxNumber(A, N))
