arr = [1, 5, 3, 4, 2]
x = 2
count = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if abs(arr[i] - arr[j]) == x:
            # print(arr[i], arr[j])
            count += 1
print(count)
