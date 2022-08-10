def minimum_pluses(A):
    count = [0, 0]
    lis = A.split('=')
    lhs = lis[0]
    x = []
    rhs = lis[1]
    temp = []
    for i in range(len(lhs)):
        res = []
        # x = slice(i)
        # y = slice(i+1)
        res.append(lhs[i:i+1])
        res.append(lhs[i+1:])
        temp.append(res)
    print(temp)
    return min(count)


def main():
    A = '230=32'
    result = minimum_pluses(A)
    print(result)


main()
