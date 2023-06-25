    from itertools import permutations
    n=input()
def sieve(n):
        s = xrange(3, n + 1, 2)
        r = set(s)
        [r.difference_update(xrange(n << 1, s[-1] + 1, n)) for n in s if n in r]
        return r.union([2])
    A=sieve(int(n))
    C=[]
    for x in A:
        if n%x==0:
            t=n
            c=0
            while t%x==0:
                t/=x
                c+=1
            C.append((x,c))
    D=[]
    if len(C)>=3:
        D.append([C[0][0]**C[0][1],C[1][0]**C[1][1],C[2][0]**C[2][1]])
    elif len(C)==2:
        D.append([C[0][0]**C[0][1],C[1][0]**C[1][1],1])
        for i in range(1,C[0][1]):
            D.append([C[0][0]**i,C[0][0]**(C[0][1]-i),C[1][0]**C[1][1]])
        for i in range(1,C[1][1]):
            D.append([C[1][0]**i,C[1][0]**(C[1][1]-i),C[0][0]**C[0][1]])
    elif len(C)==1:
        for i in range(C[0][1]+1):
            for j in range(C[0][1]-i+1):
                D.append([C[0][0]**i,C[0][0]**j,C[0][0]**(C[0][1]-i-j)])
    D.append([n,1,1])
    ma=-1
    mi=100000000000000000000
    for x in D:
        E=permutations(x)
        for y in E:
            t=(y[0]+1)*(y[1]+2)*(y[2]+2)-n
            ma=max(ma,t)
            if t>0:
                mi=min(mi,t)
    print mi,ma