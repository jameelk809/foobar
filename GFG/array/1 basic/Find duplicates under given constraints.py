"""
Given a sorted array A[] having 10 elements which contain 6 different
numbers in which only 1 number is repeated five times. Your task is to
find the duplicate number using two comparisons only.
"""


def findDuplicate(A):
    #   taking >2 comparisions
    """
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return int(A[i])
    """

    #   taking 1 comparision
    n = len(A) // 2
    if A[n] == A[n + 1]:
        return A[n]
    else:
        return A[n - 1]


A = [1, 2, 3, 3, 3, 3, 3, 5, 9, 10]
print(findDuplicate(A))
