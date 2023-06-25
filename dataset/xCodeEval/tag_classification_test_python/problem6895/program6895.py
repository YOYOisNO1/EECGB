    x0, y0 = map(int, input().split())
    n = input()
    
    
def cdist(x, y):
        return x * x + y * y
    
    
    d0 = [0] * n
    d1 = [[0] * n for i in xrange(n)]
    d2 = []
    
    
    
    for i in xrange(n):
        x, y = map(int, input().split())
        d0[i] = cdist(x - x0, y - y0)
    
        for j in xrange(i):
            d1[i][j] = cdist(x - d2[j][0], y - d2[j][1])
            d1[j][i] = d1[i][j]
    
        d2.append((x,y))
    
    
    
    a = [None] * (1 << n)
    a[0] = 0
    p2 = [0] * (1 << n)
    
    for i in xrange(1 << n):
        if a[i] is not None:
            for j in xrange(n):
                if i & (1<<j) == 0:
                    
                    t = i +(1<<j)
    
                    if not a[t] or a[t] > a[i] + d0[j] * 2:
                        a[t] = a[i] + d0[j] * 2
                        p2[t] = i
    
                    for k in xrange(j + 1, n):
                        if t &(1<<k) == 0:
                            t2 = t + (1<<k)
                            c = a[i] + d0[j] + d1[j][k] + d0[k]
                            if not a[t2] or a[t2] > c:
                                a[t2] = c
                                p2[t2] = i
                    break
    
    z = (1 << n) - 1
    print(a[z])
    
    r = [0]
    while z > 0:
        t = z - p2[z]
        while t:
            x = -t & t
            t -= x
            i = 0
    
            while x > 0:
                i += 1
                x /= 2
            r.append(i)
    
        z = p2[z]
        r.append(0)
    
    print(' '). join(map(str,r))