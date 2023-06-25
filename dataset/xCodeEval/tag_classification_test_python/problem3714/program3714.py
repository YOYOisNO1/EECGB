def program3714():
    n, m = map(int, input().split())
    a = map(int, input().split())
    a = [(a[i*2], a[i*2+1]) for i in xrange(n)]
    b = map(int, input().split())
    b = [(b[i*2], b[i*2+1]) for i in xrange(m)]
    ac = []
    bc = []
    for u in a:
        s = set()
        for v in b:
            t = set(u) & set(v)
            if len(t) == 1:
                s |= t
        ac.append(s)
    for u in b:
        s = set()
        for v in a:
            t = set(u) & set(v)
            if len(t) == 1:
                s |= t
        bc.append(s)
    f = 1
    sa = set()
    for s in ac:
        if len(s) == 1:
            sa |= s
        elif len(s) > 1:
            f = 0
    sb = set()
    for s in bc:
        if len(s) == 1:
            sb |= s
        elif len(s) > 1:
            f = 0
    if f and len(sa) == 1 and len(sb) == 1:
        print(sa.pop())
    elif f:
        print(0)
    else:
        print(-1)