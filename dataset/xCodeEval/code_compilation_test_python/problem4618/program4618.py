    from collections import defaultdict
    letters = 'ACGT'
    P = 10**9 + 9
    n,m = map(int,input().split())
    v = [input() for _ in xrange(m)]
    d = {(0,''):0}
    c = 1
    a = defaultdict(dict)
def f(k,s):
        global c
        if (k,s) not in d:
            d[k,s]=c
            c+=1
        return d[k,s]
    for s in v:
        for j in xrange(len(s)):
            for k in xrange(j+1):
                x = f(k,s[:j+1])
                a[f(k,s[:j])][s[j]] = x
    
    for p,s in d.keys():
        for x in letters:
            z = s+x
            for j in xrange(1,len(z)):
                op = p-j
                if s in v: op = len(z)-j-1
                f = op,z[j:]
                if f in d:
                    #print p,s,'->',f
                    a[d[p,s]][x]=d[f]
                    break
    #print d
    #print a
    d0,v0 = d,v
    d = defaultdict(int)
    d[0] = 1
    for i in xrange(n):
        dn = defaultdict(int)
        for j in xrange(c):
            for x,v in a[j].iteritems():
                dn[v]+=d[j]
                dn[v]%=P
        #print ' '.join('%s=%d'%([i for i,j in d0.iteritems() if j==k][0],v) for k,v in dn.iteritems() if v)
        d = dn
    
    print sum(d[d0[i,s]] for s in v0 for i in xrange(len(s)))