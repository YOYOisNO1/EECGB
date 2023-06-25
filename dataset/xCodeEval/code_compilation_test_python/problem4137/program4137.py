def program4137():
    f = lambda: map(int, input().split())
    n, m = f()
    p = [1 << i for i in range(n)]
    b = sum(p)
    for i in range(m):
        x, y = f()
        x -= 1
        y -= 1
        p[x] |= 1 << y
        p[y] |= 1 << x
    s = set(p)
    t = {}
    if b in s:
        t[b] = 'b'
        s.remove(b)
    if len(s) == 2:
        a, c = s
        if a | c == b and (a & c != 0) == (b in t): t[a], t[c] = 'ac'
    print('Yes\n' + ''.join(map(t.get, p)) if t else 'No')