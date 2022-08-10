def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


n = 4
arr = [1, 2, 3, 4]
lcm_set = []
for i in range(n-1):
    lcm_set.append(lcm(arr[i], arr[i+1]))
print(max(lcm_set))
