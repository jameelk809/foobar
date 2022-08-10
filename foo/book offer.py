l = [6, 4, 5, 5, 5, 5]
l.sort(reverse=True)
N = len(l)
price = 0
for i in range(N):
    x = l[i] * (i % 3 != 2 or i >= (N // 3) * 3)
    price += x
print(price)
