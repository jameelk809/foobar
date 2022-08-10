"""
A and B are good friend and programmers. They are always in a healthy
competition with each other. They decide to judge the best among them
by competing. They do so by comparing their three skills as per their
values. Please help them doing so as they are busy.

Set for A are like [a1, a2, a3]
Set for B are like [b1, b2, b3]

Compare ith skill of A with ith skill of B
if a[i] > b[i] , A's score increases by 1
if a[i] < b[i] , B's score increases by 1
if a[i] = b[i] , nothing happens
"""


def scores(a, b, cc):
    for i in range(len(a)):
        if a[i] > b[i]:
            cc[0] += 1
        elif b[i] > a[i]:
            cc[1] += 1
    return cc


A = [4, 2, 7]
B = [5, 2, 8]
C = [0, 0]
scores(A, B, C)
print(*C)

