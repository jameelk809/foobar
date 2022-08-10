"""
Given an array arr of n integers, task is to print the array in the order –
smallest number, largest number, 2nd smallest number, 2nd largest number,
3rd smallest number, 3rd largest number and so on.
"""


def rearrangeArray(Arr, n):
    res = sorted(Arr)
    i = j = 0
    while j < n-1:
        Arr[j], Arr[j+1] = res[i], res[n-i-1]
        i += 1
        j += 2
    if n % 2 != 0:
        Arr[j] = res[i]


N = 9
# [1, 9, 2, 8, 3, 7, 4, 6, 5]
Arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rearrangeArray(Arr, N)
for x in Arr:
    print(x, end=' ')

