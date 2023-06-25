    n = int(input())
    a, b, c = [], [], []
    s = input()
    from collections import defaultdict
    dp = defaultdict(lambda : float("inf"))
def count(a, st, x):
        ret = 0
        i = st
        while i < len(a) and a[i] < x:
            ret += 1
            i += 1
        return ret
    for i in xrange(len(s)):
        if s[i] == "V":
            a.append(i)
        elif s[i] == "K":
            b.append(i)
        else :
            c.append(i)
    dp[(0,0,0,0)] = 0
    for i in xrange(len(a)+1):
        for j in xrange(len(b)+1):
            for k in xrange(len(c)+1):
                for p in xrange(2):
                    if i < len(a):
                        dp[(i+1,j,k,1)] = min(dp[(i+1,j,k,1)], dp[(i,j,k,p)] + count(a,i,a[i])+count(b,j,a[i])+count(c,k,a[i]))
                    if j < len(b) and p == 0:
                        dp[(i,j+1,k,0)] = min(dp[(i,j+1,k,0)], dp[(i,j,k,p)]+count(a,i,b[j])+count(b,j,b[j])+count(c,k,b[j]))
                    if k < len(c):
                        dp[(i,j,k+1,0)]=min(dp[(i,j,k+1,0)],dp[(i,j,k,p)]+count(a,i,c[k])+count(b,j,c[k])+count(c,k,c[k]))
    print min(dp[(len(a),len(b),len(c),0)],dp[(len(a),len(b),len(c),1)])