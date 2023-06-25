def program2275():
    for _ in xrange(input()):
        x = input().strip()
        n = int(x[0])
        print((n) - 1) * 10 + sum(i for i in range(1, len(x)+1))