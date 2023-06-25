def program1008():
    import sys
    
    sl = sl = input().split()
    n = int(sl[0])
    k = int(sl[1])
    
    ks = []
    for i in range(2, k+1):
        ks.append(i)
    off = 0
    res = 0
    while n > 0 and len(ks) > 0:
        if sum(ks)-len(ks)+1 < n:
            res = -1
            break
        m = max(ks)
        rem = min(m, n+off)
        if ks.count(rem):
            n -= rem-off
            ks.remove(rem)
            off = max(off, 1)
            res += 1
    if n != 0:
        res = -1
    print res