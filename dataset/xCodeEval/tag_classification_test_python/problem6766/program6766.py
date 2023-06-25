    N=5050
    M=998244353
    p=[1]*N
    for i in range(1,N):
        p[i]=p[i-1]*i%M
def go(a,b):
        if a<b:
            a,b=b,a
        s=0
        for x in range(b+1):
            s+=p[a]*p[b]*pow(p[x]*p[a-x]*p[b-x]%M,M-2,M)
        return s%M
    a,b,c=map(int,input().split())
    print(go(a,b)*go(b,c)*go(c,a)%M)