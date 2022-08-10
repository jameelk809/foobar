def printing_results(s1, s2, s3, r, c):
    print(s1)
    print(s2)
    print(s3)
    for i in range(r - 1):
        print('|' + ('.|' * c))
        print('+' + ('-+' * c))


def starting_here():
    t = int(input())
    for j in range(1, t + 1):
        print('Case #' + str(j) + ':')
        r, c = map(int, input().split())
        s1 = '..+' + ('-+' * (c - 1))
        s2 = '..|' + ('.|' * (c - 1))
        s3 = '+-+' + ('-+' * (c - 1))
        printing_results(s1, s2, s3, r, c)


if __name__ == '__main__':
    starting_here()
