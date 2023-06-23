def f(x, t):
        d = int(x) * (10 ** (len(t[0]) - 1))
        p = [(d, d)]
        for i in t:
            u, v = [y for y in i if y >= x], [y for y in i if y < x]
            d = []
            if u:
                u = min(u)
                u = [u] + sorted(list(i - {u}))
                u = int(''.join(u))
                d.extend((a, max(b, u)) for a, b in p)
            if v:
                v = max(v)
                v = [v] + sorted(list(i - {v}), reverse = True)
                v = int(''.join(v))
                d.extend((min(a, v), b) for a, b in p)
            p = d
        return min(b - a for a, b in p)
    
    n, k = map(int, input().split())
    t = [set(input()) for i in range(n)]
    p = {i for i in '0123456789' if all(i in j for j in t)}
    s = [z - p for z in t]
    ans = min(f(x, t) for x in '0123456789')
    for x in p:
        y = p - {x}
        s = [z - y for z in t]
        ans = min(min(f(x, t) for x in '0123456789'), ans)
    print(ans)