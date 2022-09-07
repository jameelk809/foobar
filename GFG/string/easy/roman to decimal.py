def romanToDecimal(S):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum1 = dic[S[-1]]
    for i in range(len(S) - 2, -1, -1):
        if dic[S[i]] >= dic[S[i + 1]]:
            sum1 += dic[S[i]]
        else:
            sum1 -= dic[S[i]]
    return sum1


s = 'V'
print(romanToDecimal(s))
