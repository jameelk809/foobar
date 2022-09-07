def ispar(x):
    # code here
    stack = []
    # stack = deque()
    for i in range(0, len(x)):
        # print(stack)
        # print(x[i])
        if len(stack) > 0:
            if \
                    ('{' == stack[-1] and '}' == x[i]) \
                            or ('[' == stack[-1] and ']' == x[i]) \
                            or ('(' == stack[-1] and ')' == x[i]):
                stack.pop()
            elif \
                    ('}' == stack[-1] and '{' == x[i]) \
                            or (']' == stack[-1] and '[' == x[i]) \
                            or (')' == stack[-1] and '(' == x[i]):
                stack.pop()
            else:
                stack.append(x[i])
        else:
            stack.append(x[i])
    # print(stack)
    if len(stack) > 0:
        return False
    else:
        return True


par = '([]'
print(ispar(par))
