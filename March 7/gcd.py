N = 4
A = [2, 4, 6, 8]
lis = []
gcd_list = []
for i in range(N):
    for j in range(i + 1, N):
        res = [A[i], A[j]]
        lis.append(res)
print(lis)


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


for pair in lis:
    print(pair)
    gcd_list.append(GCD(pair[0], pair[1]))

print(gcd_list)