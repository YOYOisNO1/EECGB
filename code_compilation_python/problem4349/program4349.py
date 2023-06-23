def program4349():
    n, m, c, d = map(int, input().split())
    t = [(d / c, 1000, 1, c, d)] + [0] * m
    for i in range(1, m + 1):
        a, b, c, d = map(int, input().split())
        t[i] = (d / c, a, b, c, d)
    t.sort(reverse = True)
    i = p = 0
    while i < m + 1:
        u, a, b, c, d = t[i]
        i += 1
        if n < c: continue
        k = a // b
        p += d * k
        n -= c * k
        if n < 0:
            k = (- 1 - s) // c + 1
            n += c * k
            p -= d * k
    print(p)