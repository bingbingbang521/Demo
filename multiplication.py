i, j = 1, 1
while i < 10:
    n = 1
    while n <= i:
        print("{} * {} = {}".format(i, n, i*n), end='  ')
        n += 1
    print()
    i = i+1
