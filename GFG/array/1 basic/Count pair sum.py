"""
Given two sorted arrays(arr1[] and arr2[]) of size M and N of distinct elements.
Given a value Sum. The problem is to count all pairs from both arrays whose sum is equal to Sum.
Note: The pair has an element from each array.
"""


def countPairs(arr1, arr2, M, N, x):
    # count = 0
    # for i in range(M):
    #     for j in range(N):
    #         if arr1[i] + arr2[j] == x:
    #             count += 1
    # return count
    count = 0
    i = 0
    j = N - 1
    while (i < M) and (j >= 0):
        if arr1[i] + arr2[j] == x:
            i += 1
            j -= 1
            count += 1
        elif arr1[i] + arr2[j] > x:
            j -= 1
        elif arr1[i] + arr2[j] < x:
            i += 1
    return count


m = 4
n = 4
Sum = 10
arr1 = [1, 3, 5, 7]
arr2 = [2, 3, 5, 8]
print(countPairs(arr1, arr2, m, n, Sum))
