"""
Given an array A of size n of integers in the range from 1 to n,
we need to find the inverse permutation of that array.
Inverse Permutation is a permutation which you will get by inserting position
of an element at the position specified by the element value in the array.
For better understanding, consider the following example:
Suppose we found element 4 at position 3 in an array, then in reverse permutation,
we insert 3 (position of element 4 in the array) in position 4 (element value).
"""


def inversePermutation(arr, n):
    res = [0] * n
    # for item in arr:
    #     arr[item-1] = arr.index(item)+1
    for i in range(0, n):
        res[arr[i] - 1] = i + 1
    return res


A = [2, 3, 4, 5, 1]
N = 5
print(inversePermutation(A, N))
