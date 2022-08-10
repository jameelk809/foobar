"""
Given a sorted array of size N and an integer K, find the
position at which K is present in the array using binary search.
"""


def binarysearch(arr, n, k):
    if not arr:
        return -1
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


n = 5
arr = [11, 22, 33, 44, 55]
k = 445
print(binarysearch(arr, n, k))
