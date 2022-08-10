def clsarrange(s):
    N = len(s)
    g = 0
    b = 0
    for i in range(N):
        if s[i] == 'G':
            g += 1
        else:
            b += 1
    if g > b + 1 or b > g + 1:
        return -1
    if N % 2:
        num = (N + 1) / 2
        g_even = 0
        b_even = 0
        for i in range(N):
            if i % 2 == 0:
                if s[i] == 'G':
                    g_even += 1
                else:
                    b_even += 1
        if g > b:
            return int(num - g_even)
        else:
            return int(num - b_even)
    else:
        g_odd = 0
        g_even = 0
        for i in range(N):
            if s[i] == 'G':
                if i % 2:
                    g_odd += 1
                else:
                    g_even += 1
        return min(N // 2 - g_odd, N // 2 - g_even)


s = input()
print(clsarrange(s), end="")
