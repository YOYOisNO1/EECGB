def _cmp(x, y):
        c = -cmp(x[1][0], y[1][0])
        d = -cmp(x[1][1]-x[1][2], y[1][1]-y[1][2])
        e = -cmp(x[1][1], y[1][1])
        f = cmp(x[0][0], y[0][0])
        if c != 0:
            return c
        elif d != 0:
            return d
        elif e != 0:
            return e
        else:
            return f
    
    results = {}
    for i in range(5):
        a, b, pts = input().split()
        x, y = [int(i) for i in pts.split(':')]
        at = results[a] = results.get(a, [0, 0, 0])
        at[0], at[1], at[2] = (at[0]+(3 if x > y else 1 if x == y else 0), at[1]+x, at[2]+y)
        bt = results[b] = results.get(b, [0, 0, 0])
        bt[0], bt[1], bt[2] = (bt[0]+(3 if x < y else 1 if x == y else 0), bt[1]+y, bt[2]+x)
    
    b = tuple(results['BERLAND'])
    c = tuple(results['CERLAND'])
    del results['BERLAND']
    del results['CERLAND']
    results = list(results.items())
    
    (x, y) = (10, -1)
    
    for i in xrange(10):
        for j in xrange(i):
            res = results[:]
            res.append(('BERLAND', (b[0]+3, b[1]+i, b[2]+j)))
            res.append(('CERLAND', (c[0], c[1]+j, c[2]+i)))
            res.sort(_cmp)
            barland = None
            if res[0][0] == 'BERLAND': 
                barland = res[0][1]
            elif res[1][0] == 'BERLAND':
                barland = res[1][1]
            if barland and i-j < x - y: 
                (x, y) = i, j
                
    if x == 10 and y == -1:
        print 'IMPOSSIBLE'
    else:
        print '{0}:{1}'.format(x, y)