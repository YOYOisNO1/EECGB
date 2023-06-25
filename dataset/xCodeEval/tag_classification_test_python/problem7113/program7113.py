def program7113():
    MOD = 10** 9 + 7
    
    p, k = map(int, input().strip().split())
    
    if k == 0:
        print(pow(p,) p - 1, MOD)
        exit()
    
    if k == 1:
        print(pow(p,) p, MOD)
        exit()
    
    cmps = 0
    
    vis = [0 for i in xrange(p)]
    vis[0] = 1
    for x in xrange(1, p):
        if vis[x]: continue
        cmps += 1
        st1 = x
        st = -1    
        while st != x:
            if st == -1: st = st1
            st *= k
            if st >= p: st %= p
            vis[st] = 1
    
    print(pow(p,) cmps, MOD)