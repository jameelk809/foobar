n = 15
binary = ''
while n > 0:
    r = n % 2
    n //= 2
    binary = str(r) + binary

XOR_result = ''
for i in range(0, len(binary)-1):
    XOR_result += str(int(binary[i]) ^ int(binary[i + 1]))
XOR_result += str(int(binary[-1]) ^ 1)
res = 0
for i in range(len(XOR_result)):
    res += int(XOR_result[i]) * 2 ** (len(XOR_result) - 1 - i)
print(res)


"""-------------------------------------------------"""


def fun(n):
    arr = [0] * n
    temp = [0] * n
    t = 0
    base = 1
    index = 0
    while n != 0:
        arr[index] = n % 2
        n = int(n / 2)
        index = index + 1
    print("decimal in reverse: ", arr)
    temp[0] = arr[0] ^ 1
    for i in range(1, index):
        x, y = arr[i], arr[i-1]
        temp[i] = arr[i] ^ arr[i-1]
    print("X in reverse: ", temp)
    for i in range(0, index):
        t = t + (temp[i] * base)
        base = base * 2

    return t


fun(649)