# Armstrong


# x = 371
x = 407
sum_of_cubes = 0

for digit in str(x):
    sum_of_cubes += int(digit)**3

if x == sum_of_cubes:
    print("Armstrong")
else:
    print("not Armstrong")
