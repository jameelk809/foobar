"""A supermarket maintains a pricing format for all its products. A value N is printed on each product. When the
scanner reads the value N on the item, the product of all the digits in the value N is the price of the item. The
task here is to design the software such that given the code of any item N the product (multiplication) of all the
digits of value should be computed(price). """

n = 5244
prod = 1
for dig in str(n):
    prod *= int(dig)
print(prod)

