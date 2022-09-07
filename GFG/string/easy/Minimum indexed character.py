def minIndexChar(Str, pat):
    lis = []
    for x in pat:
        if x not in Str:
            continue
        lis.append(Str.index(x))
    if len(lis) == 0:
        return -1
    else:
        return min(lis)


Str = 'geeksforgeeks'
patt = 'set'
print(minIndexChar(Str, patt))
