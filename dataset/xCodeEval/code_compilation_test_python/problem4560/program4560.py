    o = map(int, input().split())
    n = int(input())
    c = [map(int, input().split()) for _ in range(n)]
    d = [None] * (1 << n)
    p = [0] * (1 << n)
    z = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    pw = [(1 << i) for i in xrange(n + 1)]
    
    
def dist(i, j):
        if z[i + 1][j + 1] == -1:
            a = o if i < 0 else c[i]
            b = o if j < 0 else c[j]
            z[i + 1][j + 1] = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        return z[i + 1][j + 1]
    
    
def upd(im, res, pr):
        if d[im] is None or res < d[im]:
            p[im] = pr
            d[im] = res
    
    
def dp(msk):
        if d[msk] is None:
            return
        idx = -1
        for i in range(n):
            if not (msk & pw[i]):
                im = msk + pw[i]
                for j in range(i, n):
                    if not (msk >> j & 1):
                        r = dist(i, j) + dist(i, -1) + dist(j, -1)
                        jm = im + (pw[j] if i != j else 0)
                        upd(jm, r + d[msk], msk)
                break
    
    
    d[0] = 0
    for i in range(1 << n):
        dp(i)
    msk = (1 << n) - 1
    print d[msk]
    
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
            r.append(t + 1)
        msk = p[msk]
        r.append(0)
    print ' '.join(map(str, r))