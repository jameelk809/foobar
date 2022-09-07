def reverseWords(S):
    # code here
    S = S.split('.')
    S = S[::-1]
    S = ".".join(S)
    return S


S = 'pqr.mno'
print(reverseWords(S))
