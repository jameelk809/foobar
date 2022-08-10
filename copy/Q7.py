def isPrime(n):
    flag = False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                flag = True
                break
    else:
        # print("otherwise")
        return 0
    if flag:
        # print("composite")
        return 0
    else:
        # print("prime")
        return 1


def prime_composite_list(lst):
    prime = []
    composite = []
    output = []
    for number in lst:
        if isPrime(number):
            prime.append(number)
        else:
            composite.append(number)
    output.append(prime)
    output.append(composite)
    return output


# tst = [11, 7, 90, 44, -9]
# ttt = prime_composite_list(tst)
# print(ttt)
# isPrime(11)

if __name__ == '__main__':
    l = []
    count = int(input())
    for i in range(count):
        l.append(int(input()))
    print(prime_composite_list(l))
