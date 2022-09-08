def winner(arr, n):
    d = {}
    l = []
    max1 = -1
    for i in arr:
        d[i] = d.get(i, 0) + 1
    for i in d:
        if d[i] > max1:
            max1 = d[i]
    for i in d:
        if d[i] == max1:
            l.append(i)
    g = min(l)
    return g, d[g]


Votes = ['john', 'johnny', 'jackie', 'johnny', 'john' 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
print(winner(Votes, len(Votes)))
