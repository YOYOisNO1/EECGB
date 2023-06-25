def program4069():
    a = [0]*10
    b = [0]*10
    s = map(int, list(input()))
    n = len(s)
    c1=['']*n
    c2=['']*n
    for i in range(n):
        a[s[i]] += 1
        b[s[i]] += 1
    
    n-=1
    
    while (a[0]-a[9])>0:
        c1[n]=c2[n] = str(0)
        a[0]-=1
        b[0]-=1
        n-=1
    
    k = [i for i in range(1,6) if a[i]*b[10-i]>0]
    
    d = {}
    for l in k:
        o = 0
        a[l]-=1
        b[10-l]-=1
        for i in range(10):
            o += min(a[i], b[9-i])
        d[o] = l
        a[l]+=1
        b[10-l]+=1
    
    if d.keys():
        t = d[max(d.keys())]
        a[t] -= 1
        b[10-t] -= 1
        c1[n]=str(t)
        c2[n]=str(10-t)
        n -= 1
    
    for i in range(10):
        if a[i]*b[9-i]>0:
            m = 0
            while (a[i]*b[9-i]>0):
                a[i]-=1
                b[9-i]-=1
                m+=1
            for j in range(m):
                c1[n]=str(i)
                c2[n]=str(9-i)
                n-=1
    
    m = n
    
    for i in range(10):
        while a[i]>0:
            c1[n] = str(i)
            n-=1
            a[i] -= 1
        while b[i]>0:
            c2[m] = str(i)
            m-=1
            b[i] -= 1
    
    
    c1 = ''.join(str(n) for n in c1)
    c2 = ''.join(str(n) for n in c2)
    print c1
    print c2