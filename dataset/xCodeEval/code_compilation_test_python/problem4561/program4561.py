    o = map(int, input().split())
    n = int(input())
    c = [map(int, input().split()) for _ in range(n)]
    INF = 10 ** 6
    d = [INF for _ in range(1 << n)]
    p = [None for _ in range(1 << n)]
    z = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    
    
def dist(i, j):
        if z[i + 1][j + 1] == -1:
            a = o if i < 0 else c[i]
            b = o if j < 0 else c[j]
            z[i + 1][j + 1] = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        return z[i + 1][j + 1]
    
    
def upd(im, res, pr):
        if res < d[im]:
            p[im] = pr
            d[im] = res
    
    
def dp(msk):
        if d[msk] == INF:
            return
        idx = -1
        for i in range(n):
            if msk & (1 << i) == 0:
                im = msk | (1 << i)
                for j in range(i, n):
                    if msk & (1 << j) == 0:
                        r = dist(i, j) + dist(i, -1) + dist(j, -1)
                        jm = im | (1 << j)
                        upd(jm, r + d[msk], msk)
                break
    
    
    d[0] = 0
    for i in range(1 << n):
        dp(i)
    msk = (1 << n) - 1
    print d[msk]
    
    r = [0]
    while p[msk]:
        m = msk & p[msk]
        for t in range(n):
            if (1 << t) & m:
                r.append(t + 1)
        r.append(0)
        msk = p[msk]
        r.append(0)
    print ' '.join(str(t) for t in r)