# print total number of prime and composite numbers within a range

lower, upper = 1, 100
prime = composite = 0


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for num in range(lower, upper + 1):
    if num == 1:
        continue    # neither prime nor composite
    if isPrime(num):
        prime += 1
    else:
        composite += 1
print("total number of primes: ", prime)
print("total number of composites: ", composite)
