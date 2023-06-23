def program3177():
    k, n, m = map(int, input().split())
    a = map(int, input().split())
    s = sum(a)
    a.sort()
    ans = 0
    for i in xrange(m / s + 1):
        p = i * (n + 1)
        t = m - i * s
        for x in a:
            if t >= x * (k - i):
                t -= x * (k - i)
                p += k - i
            else:
                p += t / x
                break
        if ans < p:
            ans = p
    print ans