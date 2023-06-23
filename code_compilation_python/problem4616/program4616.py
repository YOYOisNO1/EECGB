    from collections import defaultdict
    letters = 'ACGT'
    P = 10**9 + 9
    n,m = map(int,input().split())
    v = [input() for _ in xrange(m)]
    d = {(0,''):0}
    di = {0:(0,'')}
    c = 1
    a = defaultdict(dict)
    t = set(v)
def f(k,s):
        global c
        if (k,s) not in d:
            d[k,s]=c
            di[c]=k,s
            c+=1
        return d[k,s]
def add(f,l,t):
        global a
        if l not in a[f] or di[a[f][l]][0]<di[t][0]:
            #print di[f], '->', di[t]
            a[f][l]=t
    for s in v:
        for j in xrange(len(s)):
            for k in xrange(j+1):
                if j==len(s)-1: add(f(k,s[:j]),s[j],f(len(s),s[:j+1]))
                else: add(f(k,s[:j]),s[j],f(k,s[:j+1]))
    
    for p,s in d.keys():
        for x in letters:
            z = s+x
            fm = False
            for j in v:
                if z.endswith(j) and p+len(j)>=len(z):
                    fm = True
                    break
            for j in xrange(len(z)):
                f = p-j,z[j:]
                if fm: f = len(z[j:]),z[j:]
                if f in d:
                    add(d[p,s],x,d[f])
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
        #print ' '.join('%s=%d'%(di[k],v) for k,v in dn.iteritems() if v)
        d = dn
    
    #print [di[k] for k,v in d.iteritems() if di[k][0]==len(di[k][1])]
    print sum(v for k,v in d.iteritems() if di[k][0]==len(di[k][1]))%P