"""
You are given an array Arr of size N. Replace every element with the next
greatest element (the greatest element on its right side) in the array.
Also, since there is no element next to the last element, replace it with -1.
"""


def nextGreatest(arr, n):
    # for i in range(n-1):
    #     arr[i] = max(arr[i+1:])
    # arr[-1] = -1
    m = arr[n - 1]
    arr[n - 1] = -1
    for i in range(n - 2, -1, -1):
        temp = arr[i]
        arr[i] = m
        m = max(m, temp)


N = 6
A = [16, 17, 4, 3, 5, 2]
nextGreatest(A, N)
print(*A)
