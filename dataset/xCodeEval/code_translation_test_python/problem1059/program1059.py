def program1059():
    n,m=map(int,input().split())
    co=[0 for i in xrange(101)]
    for i in map(int,input().split()): co[i] += 1
    f=False
    for t in xrange(m, 0, -1):
        have = 0
        for i in co:
            have += i / t
        if have >= n:
            f = True
            ans = t
            break
    if not f:
        ans = 0
    print(ans)