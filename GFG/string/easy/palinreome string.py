def isPalindrome(S):
    # code here
    if S == S[::-1]:
        return 1
    else:
        return 0


S = "abc"
print(isPalindrome(S))
