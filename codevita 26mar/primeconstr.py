# prime construction

from math import gcd

l = list(map(int, input().split()))
q = min(l)
lcm = 1
for i in l:
    lcm = lcm * i // gcd(lcm, i)
r = lcm + q
a = 2
while r > a:
    if r % a == 0 & a != r:
        print("None", end="")
        a = a + 1
        break
    else:
        print(r, end="")
        a = r + 1
