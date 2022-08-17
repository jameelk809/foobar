# A Number that is divisible by the sum of its digits is known as a Harshad number


# N = 21
N = 1729

N = str(N)
s = 0
for i in range(len(N)):
    s += int(N[i])
if int(N) % s == 0:
    print("Harshad no.")
else:
    print("Not a Harshad no.")

