def root(a):
        res = 0
        while a>0:
            res+=a%10
            a/=10
        return root(res) if res>9 else res
    
    n = int(input())
    t = [0 for i in xrange(0,10)]
    for i in xrange(1,n+1):
        t[root(i)]+=1
    ans1 = 0
    #print t
    for r1,i in enumerate(t):
        for r2,j in enumerate(t):
            for r3,k in enumerate(t):
                if r3==root(r2*r1):
                    #if i*j*k>0 : print r1,r2,r3
                    ans1+=i*j*k
    ans2 = 0
    for i in xrange(1,n+1):
        ans2+=n/i
    #print [(i,j) for (i,j) in enumerate(t)]
    #print root(1)
    #print ans1
    print ans1-ans2