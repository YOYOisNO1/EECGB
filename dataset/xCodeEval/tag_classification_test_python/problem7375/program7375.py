def program7375():
    f = lambda: map(int, input().split())
    n, m = f()
    p = [1 << i for i in range(n)]
    for i in range(m):
        x, y = f()
        x -= 1
        y -= 1
        p[x] |= 1 << y
        p[y] |= 1 << x
    s = set(p)
    b = (1 << n) - 1
    t = {}
    if b in s:
        t[b] = 'b'
        s.remove(b)
    if len(s) == 2:
        a, c = s
        if a | c == b and bool(a & c) == (b in t):
            t[a], t[c] = 'ac'
            s.clear()
    print('No' if s else 'Yes\n' + ''.join(map(t.get, p)))