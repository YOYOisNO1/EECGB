def program4684():
    global debug
    debug = 0
    
    line = map(int, input().split())
    n = line[0]
    k = line[1]
    m = line[2]
    
    r = [[0 for _ in xrange(k)] for _ in xrange(n)]
    t = [[0 for _ in xrange(k)] for _ in xrange(n)]
    
    for i in xrange(10):
        r[0][i % k] += 1
    
    base = 1
    for i in xrange(1, n):
        base *= 10
        if (i == n - 1): start = 1
        else: start = 0
        for c in xrange(start, 10):
            offset = (c * base) % k
            for j in xrange(k):
                #for pre in xrange(i):
                r[i][j] += r[i - 1][(j - offset) % k]
                r[i][j] %= m
    if (debug >= 2): print r
    
    t[0][0] = (r[0][0] - 1) % m
    base = 1
    for i in xrange(1, n):
        base *= 10
        t[i][0] = r[i][0]
        if (i == n - 1):
            start = 1
        else:
            start = 0
            t[i][0] -= 1
        for c in xrange(start, 10):
            offset = (c * base) % k
            for j in xrange(k):
                idx = (offset + j) % k
                if (idx != 0):
                    t[i][idx] += t[i - 1][j]
                    t[i][idx] %= m
    if (debug >= 2): print t
    print sum(t[n - 1]) % m