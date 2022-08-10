t = [[12121, 15, 5], [12311, 5, 10], [17215, 2, 3]]
f = 12311
minn = t[0][1]
mintrain = 0
d = {}
platform = 1
clock = 0
for tr in t:
    if tr[1] < minn:
        minn = tr[1]
        mintrain = tr[0]
d[mintrain] = platform
platform += 1
clock += minn
print(d)

