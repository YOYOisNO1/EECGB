def program4617():
    from collections import defaultdict
    letters = 'ACGT'
    P = 10**9 + 9
    n,m = map(int,input().split())
    v = [input() for _ in xrange(m)]
    d = {'':0}
    c = 1
    a = defaultdict(dict)
    for s in v:
        p = 0
        for j in xrange(len(s)):
            x = s[:j+1]
            if x not in d:
                d[x]=c
                c+=1
            a[p][s[j]]=d[x]
            p = d[x]
    for s in v:
        for x in letters:
            z = s+x
            for j in xrange(len(z)):
                if z[j:] in d:
                    a[d[s]][x]=d[z[j:]]
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
        #print dn
        d = dn
    
    print sum(d[d0[s]] for s in v0)