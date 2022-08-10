"""
Given a stream of incoming numbers, find average or mean of the stream at every point.
"""


def streamAvg(arr, n):
    res = []
    s = 0
    for i in range(n):
        s += arr[i]
        res.append(s/(i+1))
    return res


A = [10, 20, 30, 40, 50]
N = 5
ans = streamAvg(A, N)
for x in ans:
    print('%.2f' % x, end='\t')
