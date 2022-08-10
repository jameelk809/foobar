def pattern(n):
    for i in range(-n//2+1, (n//2+1)):
        for j in range(-n//2, (n//2+1)):
            if abs(i) + abs(j) < n//2+1:
                print(" ", end='')
            else:
                print("*", end='')
        print()


pattern(5)

