"""
Given an array Arr of N positive integers. Your task is to find the elements
whose value is equal to that of its index value ( Consider 1-based indexing ).
"""


def valueEqualToIndex(arr, n):
    out = []
    for i in range(n):
        if arr[i] == i+1:
            out.append(i+1)
    return out


A = [15, 2, 45, 12, 7, 6, 7]
n = 7
ans = valueEqualToIndex(A, n)

if len(ans) == 0:
    print("Not Found")
else:
    for x in ans:
        print(x, end=" ")
    print()
