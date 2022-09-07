def removeDups(S):
    res = ''
    for x in S:
        if x not in res:
            res += x
    return res


S = "zvvo"
print(removeDups(S))
