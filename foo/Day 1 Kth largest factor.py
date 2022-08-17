# kth factor of a number

N, k = 12, 3
count = 0
for i in range(N, 0, -1):
    if N % i == 0:
        count += 1
    if count == k:
        print(i)
        break

