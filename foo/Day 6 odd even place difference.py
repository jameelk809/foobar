# day 6
# find difference between the sum of odd & even position digits

x = 5476
# x = 9834698765123
odd_sum = even_sum = 0
x = str(x)
for i in range(len(x)):
    if (i+1) % 2 == 0:
        even_sum += int(x[i])
    else:
        odd_sum += int(x[i])

print(abs(odd_sum - even_sum))
