"""
Given an array of length N, at each step it is reduced by 1 element.
In the first step the maximum element would be removed, while in the second step
minimum element of the remaining array would be removed, in the third step again
the maximum and so on. Continue this till the array contains only 1 element.
And find the final element remaining in the array.
"""


def leftElement(arr, n):
    # i = 0
    # arr.sort()
    # while n > 1:
    #     arr.remove(arr[-1])
    #     n -= 1
    #     arr.remove(arr[0])
    #     n -= 1
    # return arr
    arr.sort()
    size = len(arr) // 2
    if n % 2 == 0:
        return arr[size - 1]
    else:
        return arr[size]


A = [7, 8, 3, 4, 2, 9, 5]
N = 7
print(leftElement(A, N))
