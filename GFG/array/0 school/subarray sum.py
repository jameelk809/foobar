"""
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
"""


def subArraySum(arr, n, s):
    # for i in range(n + 1):
    #     for j in range(i):
    #         current_sum = sum(arr[j: i])
    #         if current_sum == s:
    #             return [j, i-1]
    # return [-1]
    left = 0
    right = 0
    sum = arr[0]
    while left < n and right < n:
        print(left, right)
        if sum < s:
            right += 1
            if right < n:
                sum += arr[right]
        elif sum > s:
            sum -= arr[left]
            left += 1
        else:
            return [left + 1, right + 1]
    return [-1]


N = 10
S = 12
A = [1, 2, 3, 4, 50, 6, 7, 8, 9, 10]
# A = [1, 2, 3, 7, 5]
ans = subArraySum(A, N, S)
for i in ans:
    print(i, end=" ")
