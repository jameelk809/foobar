def seriesSum(n):
    # s = 0
    # for i in range(1, n+1):
    #     s += i
    # return s
    return n*(n+1)//2

N = 5
print(seriesSum(N))
