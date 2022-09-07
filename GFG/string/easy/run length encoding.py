def encode(arr):
    # Code here
    i = 0
    count = 0
    res = ''
    while i < len(arr):
        if i + 1 < len(arr) and arr[i] == arr[i + 1]:
            count += 1
        else:
            count += 1
            res += arr[i] + str(count)
            count = 0
        i += 1
    return res


strng = 'aaaabbbccc'
print(encode(strng))
