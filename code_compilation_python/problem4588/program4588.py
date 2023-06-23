def program4588():
    n,m,k = map(int,input().split())
    rf=gf=False
    ra = []
    u = 0
    for i in xrange(n):
        s = input()
        g,r = map(s.find,'GR')
        if r<0 or g<0:
            if r<0 and g<0 or '-' not in s: continue        
            if r<0: gf=True
            else: rf=True
            continue
        u+=abs(r-g+1)%2
    u%=k+1
    if gf and rf: print "Draw"
    else:
        if u==0 and not gf: print "Second"
        else: print "First"
    
    
        