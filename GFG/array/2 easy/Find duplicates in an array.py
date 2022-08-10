"""
Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given array.
"""


def duplicates(arr, n):
    # dup = []
    # out = []
    # for item in arr:
    #     if item not in dup:
    #         dup.append(item)
    #     else:
    #         out.append(item)
    # if len(out) == 0:
    #     return -1
    # return out
    mdict = {}
    res_List = []
    for num in arr:
        if num not in mdict:
            mdict[num] = 1
        else:
            mdict[num] += 1
    print(mdict)
    for key, value in mdict.items():
        if value > 1:
            res_List.append(key)
    # return [-1] if not res_List else sorted(res_List)
    if not res_List:
        return [-1]
    else:
        return sorted(res_List)


A = [2, 3, 1, 2, 3]
N = 5
print(duplicates(A, N))
