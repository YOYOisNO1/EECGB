def program3991():
    n, a, b, c = map(int, input().split())
    print sum(n - i // 2 - 2 * j in xrange(0, b + 1) for i in xrange(0, a + 1, 2) for j in xrange(c + 1))