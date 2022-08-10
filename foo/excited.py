# def sum_till_x(x):
#     s = 0
#     while x > 0:
#         s += x
#         x -= 1
#     return s
#
#
#
# n = 828
# flag = False
#
# for i in range(n):
#     x, y = i, n-i
#     if sum_till_x(x) + sum_till_x(y) == n:
#         flag = True
#         break
# print(flag)


# Python3 program of the
# above approach

# import math
#
#
# def checkSumOfNatural(n):
#     i = 1
#     flag = False
#     while i * (i + 1) < n * 2:
#         X = i * (i + 1)
#         t = n * 2 - X
#         k = int(math.sqrt(t))
#         if k * (k + 1) == t:
#             flag = True
#             break
#         i += 1
#
#     if flag:
#         print('YES')
#     else:
#         print('NO')
#
#
# # Driver Code
# if __name__ == "__main__":
#     n = 828
#     checkSumOfNatural(n)
import math

n = int(input())
start = 1
flag = False
while start*(start+1) < n*2:
    temp = start*(start+1)
    temp2 = n*2 - temp
    temp3 = int(math.sqrt(temp2))
    if temp3*(temp3+1) == temp2:
        flag = True
        break
    start += 1
if flag:
    print("YES")
else:
    print("NO")
