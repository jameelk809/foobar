def LongestRepeatingSubsequence(str):
    s = str
    n = len(str)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if s[i] == s[j] and i != j:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]


st = "axxzxy"
print(LongestRepeatingSubsequence(st))
