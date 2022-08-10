A = [8, 8, 0, 10, 1]
a = sorted(A)
count = 0
N = len(A)
i = 0
if A == sorted(A):
    print(0)
else:
    while i < N-1:
        if A[i] > A[i+1]:
            A.remove(A[i+1])
            count += 1
            N -= 1
        else:
            i += 1
    print(count)

# def operation(A,N):
#     count=0
#     i=0
#     while i<N-1:
#         if A[i]>A[i+1]:
#             A.remove(A[i+1])
#             count+=1
#             N-=1
#         elif A[i]<A[i+1]:
#             i+=1
#     return count
#
# arr = []
# n = int(input())
# for i in range(n):
#     arr.append(int(input()))
# if arr == sorted(arr):
#     print(0)
# print(operation(arr,n))
