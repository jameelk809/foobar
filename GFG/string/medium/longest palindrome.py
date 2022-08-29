'''   Time Limit Exceeded   '''


def longestPalin(S):
    N = len(S)
    maxLen = 0
    result = ""

    for i in range(N):
        for j in range(i, N):
            temp = S[i:j + 1]
            if temp == temp[::-1] and len(temp) > maxLen:
                maxLen = len(temp)
                result = temp

    return result


S = "aaaabbaa"
print(longestPalin(S))
