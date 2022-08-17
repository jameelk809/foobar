# day 5
# pyramid with logical series
# 6,    28,  66,  120,  190,    276
# 2*3, 4*7, 6*11, 8*15, 10*19, 12*23


a, b = 2, 3
N = 5
for i in range(1, N+1):
    for j in range(1, i+1):
        res = a*b
        a += 2
        b += 4
        print("%.5d" % res, end=" ")
    print()
