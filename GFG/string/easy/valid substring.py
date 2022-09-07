def findMaxLen(S):
    # code here
    stack = [-1]
    len1 = 0

    for i in range(len(S)):
        if S[i] == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()

            if not stack:
                stack.append(i)
            else:
                len1 = max(len1, i-stack[-1])

    return len1


S = "()(())("
print(findMaxLen(S))
