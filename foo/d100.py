def starting_here():
    t = int(input())
    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))[:n]
        j = 0
        c = 0
        for p in sorted(lst):
            if p > j:
                c += 1
                j += 1
        print_result(i, c)


def print_result(k, d):
    print('Case #' + str(k + 1) + ':', d)


if __name__ == '__main__':
    starting_here()

