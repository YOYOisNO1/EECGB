def program2272():
    k, l, m, n, d = [input() for _ in xrange(5)]
    ans = 0
    for i in xrange(1, d + 1):
        t = [i % k, i % l, i % m, i % n]
        if 0 in t:
            ans += 1
    print(ans)