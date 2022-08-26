def maxXOR(a, b):
    lis = []
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            lis.append(i ^ j)
    return max(lis)


print(maxXOR(10, 15))
