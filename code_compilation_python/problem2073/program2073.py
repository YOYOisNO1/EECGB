def program2073():
    import math
    n,m=map(int,input().strip().split())
    
    f = lambda l:[1, l, 0, l-1]
    ans = [(n,m),(0,0)]
    if n == 0:
        ans = [(0, y) for y in f(m)]
    elif m == 0:
        ans = [(x, 0) for x in f(n)]
    else:
        pts = [(x, y) for x in f(n) for y in f(m)]
        d = lambda u,v: sum([(u[i]-v[i])**2 for i in [0,1]])
        cur = ans[-1]
        if math.sqrt(d(n,m)) + max(n,m) < math.sqrt(d(n-1, m)) + math.sqrt(d(n,m-1)):
            ans = 
        while len(ans) < 4:
            for p in pts:
                if p in ans: continue
                if d(cur,ans[-1]) < d(p,ans[-1]): cur = p
            ans += [cur]
    print ans
    