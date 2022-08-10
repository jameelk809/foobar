"""
done in java, 300/301 test cases passed
"""
"""
Given an array of n integers and q queries. Write a program to find
floor value of mean in range l to r for each query in a new line.
"""


def findMean(arr, queries, n, q):
    i = j = 0
    out = []
    while j < len(queries)-1:
        L = queries[j]
        R = queries[j+1]
        j += 2
        out.append(sum(arr[L:R+1])//(R-L+1))
    return out


# Arr = [1, 2, 3, 4, 5]
# Q = 3
# N = 5
# Queries = [0, 2, 1, 3, 0, 4]
Arr = [6, 7, 8, 10]
Q = 2
N = 4
Queries = [0, 3, 1, 2]
print(*findMean(Arr, Queries, N, Q))
