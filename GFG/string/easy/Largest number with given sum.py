def largestNum(n, s):
    res = ""
    if s > 9 * n:
        return -1
    else:
        x = s // 9
        res += "9" * x
        if s % 9 != 0:
            res += str(s % 9)

        while len(res) < n:
            res += "0"
        return res


N = 5
S = 12
print(largestNum(N, S))
