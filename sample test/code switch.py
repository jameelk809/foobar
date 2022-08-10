m = int(input())
A = []
for _ in range(m):
    A.append(int(input()))
n = int(input())
B = []
for _ in range(n):
    B.append(int(input()))
switch = 0
i = j = 0
website = False
application = False
if B[j] < A[i]:
    application = True
else:
    website = True
while i < m and j < n:
    if website and A[i] < B[j]:
        i += 1
    elif application and A[i] > B[j]:
        j += 1
    else:
        switch += 1
        if website and B[j] < A[i]:
            website = False
            application = True
        if application and B[j] > A[i]:
            website = True
            application = False
if website and j < n:
    switch += 1
if application and i < m:
    switch += 1
print(switch)

