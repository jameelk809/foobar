def nonrepeatingCharacter(s):
    # code here
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    for j in s:
        if dic[j] == 1:
            return j
    return '$'


s = 'hello'
print(nonrepeatingCharacter(s))
