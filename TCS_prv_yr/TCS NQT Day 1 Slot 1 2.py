# A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of
# it after the most significant bit including the most significant bit. Print the positive integer value after
# toggling all bits


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def toglng_lstmbits(gvn_numb):
    print(gvn_numb)



n = 10
x = decimalToBinary(n)
y = toglng_lstmbits(x)
