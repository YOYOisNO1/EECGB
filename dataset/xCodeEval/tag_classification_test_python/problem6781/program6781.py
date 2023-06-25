def program6781():
    import math, re, sys, string, operator, functools, fractions, collections
    sys.setrecursionlimit(10**7)
    RI=lambda x=' ': list(map(int,input().split(x)))
    RS=lambda x=' ': input().rstrip().split(x)
    dX= [-1, 1, 0, 0,-1, 1,-1, 1]
    dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
    mod=int(1e9+7)
    eps=1e-6
    pi=math.acos(-1.0)
    MAX=20
    #################################################
    n,k=RI()
    ans=0
    for i in range(1,min(k,n//2)+1):
        ans+=2*(n-2*i)+1
    print(ans)