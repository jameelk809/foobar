# def func_find(number, arr, factt):
#     if number == 0:
#         return 1
#     if arr[number] != -1:
#         return arr[number]
#     c = 0
#     for p in range(1, factt + 1):
#         if number - p >= 0:
#             c += func_find(number - p, arr, factt)
#     arr[number] = c
#     return arr[number]
#
#
# test_case = int(input())
# lis = []
# for i in range(0, test_case):
#     n, fac = input().split()
#     n = int(n)
#     fac = int(fac)
#     dp = [-1] * (n + 1)
#     res = func_find(n, dp, fac)
#     lis.append(res)
# for item in lis:
#     print(item)


def find(n,dp,fac):
    if(n==0):
        return 1
    if(dp[n]!=-1):
        return dp[n]
    c=0
    for i in range(1,fac+1):
        if(n-i>=0):
            c=(c+find(n-i,dp,fac))
    dp[n]=c
    return dp[n]
t=int(input())
l=[]
for i in range(0,t):
    n,fac=input().split()
    n=int(n)
    fac=int(fac)
    dp=[-1]*(n+1)
    l.append(find(n,dp,fac))
for k in l:
    print(k)


# number = int(input())
# def count_of_ways(n, s):
#     array_a = list(range(1, n + 1))
#     i = 0
#     count = [0 for i in range(s + 1)]
#     count[0] = 1
#     for i in range(1, s + 1):
#         for j in range(n):
#             if i >= array_a[j]:
#                 count[i] += count[i - array_a[j]]
#     return count[s]
#
#
# for _ in range(number):
#     sum, m_face = map(int, input().split())
#     res = count_of_ways(m_face, sum)
#     print(res)
