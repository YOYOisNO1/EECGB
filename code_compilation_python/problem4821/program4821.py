def program4821():
    start = input().strip()
    end = input().strip()
    k = int(input())
    if k == 0:
        if start == end:
           print 1
        else:
           print 0
        exit(0)
    L = len(start)
    ans = tmp = 0
    mod = 10 ** 9 + 7
    for i in xrange(1, L):
        if start[i:] + start[:i] == end:
            tmp += 1
    if start == end:
        p = [1, 0]
        for i in xrange(k):
            p = [p[1], (p[0] * (L-1) + p[1] * (L-2)) % mod]
        ans += p[0]
    if tmp > 0:
        p = [0, 1]
        for i in xrange(k):
            p = [p[1], (p[0] * (L-1) + p[1] * (L-2)) % mod]
        ans += p[0] * tmp % mod
    print ans % mod