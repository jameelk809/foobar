def check_prime(input_n):
    if input_n <= 1:
        return False
    for numbers in range(2, input_n):
        if input_n % numbers == 0:
            return False
    return True


def main():
    res = 1
    input_num = int(input())
    while input_num > 1:
        renumber_count = 0
        res += 1
        for items in range(input_num+1):
            if check_prime(items):
                renumber_count += 1
        input_num -= renumber_count
    print(res)


main()
