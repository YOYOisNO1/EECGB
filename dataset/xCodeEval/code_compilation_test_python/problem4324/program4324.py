def program4324():
    n, k = map(int,input().split())
    k -= 1
    off = 0
    rem = n
    while rem:
        clen = 1
        while clen<rem and k >= 1 << rem-clen-1: k -= 1 << rem-clen-1; clen+=1
        print clen+off,
        for i in range(1, clen): print i+off,
        off += clen
        rem -= clen
        