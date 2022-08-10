# def base_number(msg):
#     dec_msg = ''
#     msg = msg.split()
#     for x in range(len(msg)):
#         if msg[x] == '_':
#             dec_msg += ' '
#         elif msg[x] == '#':
#             dec_msg += msg[x+1]
#         elif msg[x-1] == '#':
#             pass
#         elif msg[x].isdigit():
#             dec_msg += chr(64+int(msg[x]))
#         else:
#             dec_msg += msg[x]
#     return dec_msg
#
#
# # code = '2 1 4 _ 3 1 20 @ # 459'
# code = '! 2 # 4 % 6'
# print(base_number(code))

# A = [16,17,4,3,5,2]
# N = 6
# out = []
# for i in range(N):
#     flag = 1
#     for j in range(i+1, N):
#         x = A[j]
#         y = A[i]
#         if x > y:
#             flag = 0
#             break
#     if flag:
#         out.append(A[i])
# print(out)


# t = "09:06"
t = "10:10"
h, m = map(int, t.split(':'))
#   speed of hour hand:     0.5 degrees per minutes
#   speed of minute hand:   6 degrees per minute
h_angle = 0.5 * (60 * h + m)
m_angle = 6 * m
ret = abs(h_angle - m_angle)
print(min(ret, (360-ret)))

