"""
You are given N ropes. A cut operation is performed on ropes such that all
of them are reduced by the length of the smallest rope. Display the number
of ropes left after every cut operation until the length of each rope is zero.
"""


def RopeCutting(arr, n):
    arr.sort()
    res = []
    for i in range(n-1):
        if arr[i] != arr[i + 1]:
            res.append(n-i-1)
    return res


Arr = [5, 1, 1, 2, 3, 5]
# Arr = [4, 0, 0, 1, 2, 4]      4
# Arr = [3, 0, 0, 0, 1, 3]      3
# Arr = [2, 0, 0, 0, 0, 2]      2
# Arr = [0, 0, 0, 0, 0, 0]
print(RopeCutting(Arr, 6))
