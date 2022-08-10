# N = int(input())
# ATM = []
# for i in range(N):
#     ATM.append(int(input()))
# X = int(input())
N = 4
ATM = [4, 12, 10, 4]
X = 30
# ATM = [1, 1]
# X = 3
count = [0, 0]
s = 0
i = 0
j = N - 1
try:
    while s <= X:
        print(s)
        s += ATM[i]
        i += 1
        count[0] += 1
    s = 0
    while s <= X:
        print(s)
        s += ATM[j]
        j -= 1
        count[1] += 1
    print(count)
    print(min(count))
except:
    print(-1)
