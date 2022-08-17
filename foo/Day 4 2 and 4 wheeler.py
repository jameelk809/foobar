# day 4
# total vehicles, v
# total wheels, w
# find no. of two-wheelers(x) & four-wheelers(y)

# x + y = v
# 2x + 4y = w
# on solving,
# y = w/2 - v
# x = v - y

v = 200
w = 540
if 2 <= w and w % 2 == 0 and v < w:
    y = w // 2 - v
    x = v - y
    print("TW=", x, "FW=", y)
else:
    print("INVALID INPUT")

