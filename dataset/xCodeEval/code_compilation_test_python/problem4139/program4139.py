def program4139():
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
    t = {b: 'b'}
    s.discard(b)
    if len(s) == 2:
        a, c = s
        if a + c == b: t[a], t[c] = 'ac'
        s = {}
    print('No' if s else 'Yes\n' + ''.join(map(t.get, p)))