"""
Given an array arr[ ] containing equal number of positive and negative elements,
arrange the array such that every positive element is followed by a negative element.
Note- The relative order of positive and negative numbers should be maintained.
"""


def arranged(a, n):
    positive = []
    negative = []
    for i in range(n):
        if a[i] > 0:
            positive.append(a[i])
        else:
            negative.append(a[i])
    j = 0
    i = 0
    while j < n:
        a[j] = positive[i]
        j += 1
        a[j] = negative[i]
        j += 1
        i += 1
    return a



N = 6
arr = [-1, 2, -3, 4, -5, 6]
print(arranged(arr, N))
