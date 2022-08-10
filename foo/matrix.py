def matr(arr):
    row = len(arr)
    col = len(arr[0])
    storage = [[0 for i in range(col+1)] for j in range(row+1)]

    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            storage[i][j] = min(storage[i+1][j], storage[i][j+1])
            maximun = storage[i][j]

            if max(row-i, col-j) <= maximun:
                continue

            foundOne = True

            for p in range(0, maximun+1):
                for q in range(0, maximun+1):
                    if arr[i+p][j+q] == 1:
                        foundOne = True
                        break
                if foundOne:
                    break

        if foundOne == True:
            storage[i][j] += 1
    return storage[i][j]


arr = [[1, 1, 0], [1, 1, 1], [1, 1, 1]]
print(matr(arr))
