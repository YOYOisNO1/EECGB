def program4338():
    n, a, b = map(int, input().strip().split())
    con = 0
    for i in xrange(1, n + 1):
        if i - 1 >= a and n - i  <= b:
            con += 1
    print con