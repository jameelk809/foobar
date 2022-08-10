# T = 'experience was ultimate'
# S = 'ew'
T = 'supreme court is the highest judicial court'
S = 'su'
c = 0
T = T.split()
for words in T:
    if S in words:
        c += 1
    else:
        for letter in words:
            if letter in S:
                if letter == S[0]:
                    c += 2
                elif letter == S[1]:
                    c += 4
print(c, end='')



# p = input("")
# q = input("")
# p = 'supreme court is the highest judicial court'
# q = 'su'
# s = ''
# p1 = list(p.split(" "))
# q1 = list(q.split(" "))
# for t in range(0, len(q1) - 1):
#     c = [0 for i in range(t, len(q1))]
# for i in p1:
#     for j in range(len(q1)):
#         k1 = 0
#         while k1:
#             m2 = c.index(m1)
#             for i in range(m2, len(c)):
#                 if c[i] == m1:
#                     if ord(q1[i]) < ord(q1[m2]):
#                         m2 = i
#                     else:
#                         m2 = c.index(m1)
#                         q1[m2], q1[t] = q1[t], q1[m2]
#     s += q1[0]
# print(len(s))
