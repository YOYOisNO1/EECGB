def program3027():
    s = (input(), input())
    p = map(lambda x: x.count('+') - x.count('-'), s)
    k = s[1].count('?')
    
    if not k:
        print 1.0
        exit()
    elif k < abs(p[0] - p[1]):
        print 0.0
        exit()
    
    f = [[0] * (2 * k + 1) for _ in xrange(k)]
    f[0][1] = f[0][-1] = 0.5
    
    for i in xrange(1, k):
        for j in xrange(-k, k + 1):
            f[i][j] = 0.5 * f[i - 1][j + 1] + 0.5 * f[i - 1][j - 1]
    
    print '%1.12f'f[k - 1][p[0] - p[1]]