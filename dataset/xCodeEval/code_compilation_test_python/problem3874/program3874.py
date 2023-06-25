def program3874():
    f = lambda: map(int, input().split())
    a, b = f()
    c, d = f()
    p = [[a, b, c, d, 0, 0]]
    n, q = -1, []
    while p:
        a, b, c, d, s, k = p.pop()
        u, v = a * b, c * d
        if u == v and (k < n or n < 0):
            n, q = k, [c, d, a, b] if s else [a, b, c, d]
            continue
        if u > v: a, b, c, d, s = c, d, a, b, 1 - s
        if c % 2 == 0: p.append((a, b, c // 2, d, s, k + 1))
        if c % 3 == 0: p.append((a, b, 2 * c // 3, d, s, k + 1))
        if d % 2 == 0: p.append((a, b, c, d // 2, s, k + 1))
        if d % 3 == 0: p.append((a, b, c, 2 * d // 3, s, k + 1))
    for t in [n] + q: print(t)