# # n = 4
# # st = ['6', 'T', '+', 'R']
# # st = []
# n = int(input())
# st = list(input().split())
# loader = []
# for item in st:
#     if item.isdigit():
#         loader.append(int(item))
#     elif item == 'R':
#         loader.pop()
#     elif item == 'T':
#         temp = loader[-1]
#         loader.append(temp*2)
#     elif item == '+':
#         temp1 = loader[-1]
#         temp2 = loader[-2]
#         loader.append(temp1+temp2)
# print(sum(loader))

# n = int(input())
# a = []
# t = []
# z = [str(i) for i in range(-1, -10, -1)]
# for i in range(n):
#     x = input()
#     if x.isdigit() or x in z:
#         t.append(int(x))
#     elif x == 'R':
#         t.pop()
#     elif x == 'T':
#         t.append(2 * int(t[-1]))
#     elif x == '+':
#         t.append(int(t[-1]) + int(t[-2]))
# print(sum(t))



