def program7131():
    MOD = 10** 9 + 7
    
    p, k = map(int, input().strip().split())
    
    cmps = 0
    
    vis = [0 for i in xrange(p)]
    
    for x in xrange(p):
        if vis[x]: continue
        
        cmps += 1
        st = x
        vis[st] = 1
        st *= k
        if st >= p: st %= p
    
        while st != x and st != 0:
            vis[st] = 1
            st *= k
            if st >= p: st %= p
    
    if k != 1: cmps -= 1
    
    print(pow(p,) cmps, MOD)