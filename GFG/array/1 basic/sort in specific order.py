"""
Given an array A of positive integers. Your task is to sort them in such a way
that the first part of the array contains odd numbers sorted in descending order,
rest portion contains even numbers sorted in ascending order.
"""


def sortIt(arr, n):
    odd = []
    even = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    odd.sort(reverse=True)
    even.sort()
    res = odd + even
    for i in range(n):
        arr[i] = res[i]


Arr = [1, 2, 3, 5, 4, 7, 10]
N = 7
sortIt(Arr, N)
print(*Arr)
