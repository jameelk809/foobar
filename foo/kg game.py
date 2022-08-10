# kindergarten game

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))


def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


n = 3
m = 2

x = nCr(n, 2) + (n + 1) - m
print(x)

