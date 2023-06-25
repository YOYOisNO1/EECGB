    o = map(int, input().split())
    n = int(input())
    c = [map(int, input().split()) for _ in xrange(n)]
    d = [None] * (1 << n)
    p = [0] * (1 << n)
    z = [[-1 for i in xrange(n + 1)] for j in xrange(n + 1)]
    pw = [(1 << i) for i in xrange(n + 1)]
    
    
def dist(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    
    for i in xrange(n):
        for j in xrange(i, n):
            z[i][j] = dist(c[i], c[j])
            z[j][i] = z[i][j]
    z0 = [dist(c[i], o) for i in xrange(n)]
    
    
    d[0] = 0
    for msk in xrange(1 << n):
        if d[msk] is not None:
            for i in xrange(n):
                if not (msk & pw[i]):
                    im = msk + pw[i]
                    for j in xrange(i, n):
                        if not (msk >> j & 1):
                            r = z[i][j] + z0[i] + z0[j] + d[msk]
                            jm = im + (pw[j] if i != j else 0)
                            if d[jm] is None or r < d[jm]:
                                p[jm] = msk
                                d[jm] = r
                    break
    msk = (1 << n) - 1
    print(d[msk])
    
    r = [0]
    while msk:
        m = msk - p[msk]
        while m:
            tt = -m & m
            m -= tt
            t = 0
            while tt > 0:
                t += 1
                tt /= 2
            r.append(t)
        msk = p[msk]
        r.append(0)
    print(' ').join(map(str, r))