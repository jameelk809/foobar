"""
You start with an array A of size N. Also, A[i] = 0 for i = 1 to N.
You will be given K positive integers. Let j be one of these integers,
you have to add 1 to all A[i], for i ≥ j. Your task is to print array
A after all these K updates are done.
"""


def update(a, n, updates, k):
    for i in range(k):
        a[updates[i] - 1] += 1
    for i in range(1, n):
        a[i] += a[i-1]


n = 3
k = 4
a = [0]*n
updates = [1, 1, 2, 3]
update(a, n, updates, k)
