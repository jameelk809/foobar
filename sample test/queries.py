# S = ['ab', 'abc', 'def', 'rf']
# Q = 'abcdef'
# S = ['iy', 'k', 'kbgb', 'j', 'qc']
# Q = 'kzy'
# S = ['ukwy']
# Q = 'sl'
n = int(input())
S = []
for i in range(n):
    S.append(input())
n1 = int(input())
Q = input()
A = []
score = 0
for item in S:
    if item in Q:
        A.append(S.index(item))
for i in range(len(A)):
    score += A[i] * 10 ** i
print(score)
