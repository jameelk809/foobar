def editDistance(s, t):
    dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]

    def op(s, t, i, j):
        if i == 0 and j == 0:
            return 0
        if i == 0 or j == 0:
            return max(i, j)
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i - 1] == t[j - 1]:
            dp[i][j] = op(s, t, i - 1, j - 1)
            return dp[i][j]
        else:
            dp[i][j] = 1 + min(op(s, t, i - 1, j - 1), op(s, t, i, j - 1), op(s, t, i - 1, j))
            return dp[i][j]

    return op(s, t, len(s), len(t))


s = 'geeks'
t = 'geesks'
print(editDistance(s, t))
