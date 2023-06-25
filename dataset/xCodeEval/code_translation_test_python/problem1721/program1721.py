def program1721():
    sl = [0]*51
    sl[0] = 1
    for i in range(1,51):
        sl[i] = sl[i-1] + (2**i)
        
    h,n = map(int,input().split())
    
    nl = []
    n += sl[h-1]
    tn = n
    nl.append(tn)
    while tn != 1:
        tn = tn//2
        nl.append(tn)
        
    ans = 0
    cn = 1
    cp = False
        
    while cn != n:
        tnl = []
        for i in range(h):
            tnl.append(cn);
            if cp == False:
                cn *= 2
            else:
                cn = cn*2+1
            cp = not cp
        if cn == n:
            ans += h
            break
        
        tnl.append(cn)
        tnl = tnl[::-1]
        for i in range(1,h+1):
            if nl[i] == tnl[i]:
                ans += sl[i-1]+h-i+1
                h=i-1
                cn=tnl[i-1]
                if cn == tnl[i]*2:
                    cn = tnl[i]*2+1
                    cp = False
                else:
                    cn = tnl[i]*2
                    cp = True
                break
    print(ans)