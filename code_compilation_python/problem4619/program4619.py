def program4619():
    from collections import defaultdict as dd
    n,m = map(int,input().split())
    l = set([input() for _ in xrange(m)])
    d = dd(set)
    for s in l:
        for i in xrange(len(s)-1): d[s[:i]].add((s[:i+1],s[i]))
        d[s[:-1]].add(('',s[-1]))
    for s in l:
        for i in xrange(1,len(s)):
            for x in l:
                if x[-i:]==s[:i]:
                    d[x[:-1]].add((s[:i],x[-1]))
    k = dd(int)
    k['']=1
    for i in xrange(n):
        kn = dd(int)
        for x,l in d.iteritems():
            for z,c in l:
                kn[z]+=k[x]
        k = kn
    print k['']