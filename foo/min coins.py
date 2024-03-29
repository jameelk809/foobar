import sys


def minCoins(n, arr, dp):
    if n == 0:
        return 0
    ans = sys.maxsize
    for i in range(len(arr)):
        if n - arr[i] >= 0:
            subAns = 0
            if dp[n-arr[i]] != -1:
                subAns = dp[n-arr[i]]
            else:
                subAns = minCoins(n - arr[i], arr, dp)
            if subAns != sys.maxsize and subAns + 1 < ans:
                ans = subAns + 1
    dp[n] = ans
    return dp[n]


n = 18
arr = [1, 5, 7]
dp = [-1]*(n+1)
dp[0] = 0
print(minCoins(n, arr, dp))
print(dp)
