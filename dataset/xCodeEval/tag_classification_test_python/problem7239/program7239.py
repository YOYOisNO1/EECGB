def program7239():
    line = map(int, input().split())
    n = line[0]
    k = line[1]
    m = line[2]
    
    t = [[0 for _ in xrange(k)] for _ in xrange(n)]
    
    #base = 1
    #for i in xrange(n):
    #    base *= 10
    #    top = base - 1
    #    r[i] = (int(top / k) + 1) % m
        #r[0][i % k] += 1
    
    #base = 1
    #for i in xrange(1, n):
        #base *= 10
        #if (i == n - 1): start = 1
        #else: start = 0
        #for c in xrange(start, 10):
            #offset = (c * base) % k
            #for j in xrange(k):
                ##for pre in xrange(i):
                #r[i][j] += r[i - 1][(j - offset) % k]
                #r[i][j] %= m
    
    t[0][0] = 9 // k
    base = 1
    for i in xrange(1, n):
        base *= 10
        if (i == n - 1):
            t[i][0] = ((10 * base - 1) // k - (base - 1) // k) % m
            start = 1
        else:
            t[i][0] = ((10 * base - 1) // k) % m
            start = 0
        baser = base % k
        offset = ((start - 1) * base) % k
        for c in xrange(start, 10):
            offset += base
            offset %= k
            for j in xrange(k):
                idx = (offset + j) % k
                if (idx != 0):
                    t[i][idx] += t[i - 1][j]
                    t[i][idx] %= m
    print(sum(t[n) - 1]) % m