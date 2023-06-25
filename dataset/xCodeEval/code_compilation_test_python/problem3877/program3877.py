def program3877():
    f = lambda: map(int, input().split())
    a, b = f()
    c, d = f()
    p = [(a, b, c, d, 0, 0)]
    n, q = -1, []
    h = set()
    while p:
        t = p.pop()
        if t in h: continue
        h.add(t)
        a, b, c, d, s, k = t
        u, v = a * b, c * d
        if u == v:
            if k < n or n < 0: n, q = k, [c, d, a, b] if s else [a, b, c, d]
            continue
        k += 1
        if u > v: a, b, c, d, s = c, d, a, b, 1 - s
        if c % 2 == 0: p += [(a, b, c // 2, d, s, k)]
        if c % 3 == 0: p += [(a, b, 2 * c // 3, d, s, k)]
        if d % 2 == 0: p += [(a, b, c, d // 2, s, k)]
        if d % 3 == 0: p += [(a, b, c, 2 * d // 3, s, k)]
    for t in [n] + q: print(t)