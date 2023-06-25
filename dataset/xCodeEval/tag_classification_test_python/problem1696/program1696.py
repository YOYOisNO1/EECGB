def program1696():
    n = int(input())
    for i in xrange(20, -1, -1):
        if n >> i:
            print(i) + 1,
            n -= 1 << i