arr = [5, 4, 3, 2, 1]
count = 0
sorted_arr = sorted(arr)
for i in range(5):
    x = arr[i]
    y = sorted_arr[i]
    if arr[i] == sorted_arr[i]:
        count += 1
print(count)
