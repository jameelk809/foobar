def se(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime
def check(f,p1,p2,prime):
    for i in range(p1,p2+1):
        for j in range(i+1,p2+1):
            if prime[i] or prime[j]:
                if f<=0:
                    print(i,j)
                    return
            else:
                if (i*j)/((j-i)**2)>=f:
                    print(i,j)
                    return
    print("None")
f,p1,p2=map(int,input().split())
prime=se(p2)
check(f,p1,p2,prime)