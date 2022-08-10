N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
i = 0
count = 0
while A != A[::-1]:
    res = A[i] + A[i+1]
    A.remove(A[i])
    A[i] = res
    i += 1
    count += 1
print(count)
