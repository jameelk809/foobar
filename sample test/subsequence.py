input = input()
num = len(input)
res = [[0 for i in range(num + 1)] for j in range(num + 1)]
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if input[i - 1] == input[j - 1] and i != j:
            res[i][j] = 1 + res[i - 1][j - 1]
        else:
            res[i][j] = max(res[i][j - 1], res[i - 1][j])
print(res[num][num])