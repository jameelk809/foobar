# TCS NQT Coding Question 2022 – September Day 1 – Slot 1

# A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N
# number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the
# conveyor belt(array).


N = 7
arr = [4, 5, 0, 1, 9, 0, 5]

j = 0
L = [0]*N
for i in range(N):
    if arr[i] != 0:
        L[j] = arr[i]
        j += 1
print(L)
