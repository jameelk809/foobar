def genIp(s):
    # Code here
    res = []
    dfs(s, 0, "", res)
    return res


def dfs(s, x, path, res):
    if x > 4:
        return
    if x == 4 and not s:
        res.append(path[:-1])
        return
    for i in range(1, len(s) + 1):
        if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
            dfs(s[i:], x + 1, path + s[:i] + ".", res)


S = '1111'
print(genIp(S))
