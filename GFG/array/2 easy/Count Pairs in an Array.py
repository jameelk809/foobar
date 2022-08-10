"""
Given an array of integers arr[0...n-1], count all pairs (arr[i], arr[j])
in it such that i*arr[i] > j*arr[j], and 0 ≤ i < j < n.
"""


def countPairs(arr, n):
    # temp = []
    # count = 0
    # for i in range(n):
    #     temp.append(i*arr[i])
    # print(temp)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         print(temp[i], temp[j])
    #         if temp[i] > temp[j]:
    #             count += 1
    # return count

    result = 0
    for i in range(n):
        j = i + 1
        while j < n:
            if i * arr[i] > j * arr[j]:
                result = result + 1
            j = j + 1
    return result


arr = [5, 0, 10, 2, 4, 1, 6]
# (10, 2) (10, 4) (10, 1) (2, 1) (4, 1)
# 20 > 6   20>16   20> 5   6>5    16>5
print(countPairs(arr, 7))
