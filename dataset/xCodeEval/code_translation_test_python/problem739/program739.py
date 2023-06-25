def program739():
    import math
    n,m=map(int,input().split())
    l=1
    r=10000000000000
    if n<=m:
        print(n)
        exit()
    while l<r:
        mid=(l+r)/2
        t=(1+mid)*mid/2
        #print(l,) r,mid,t
        if t>=n-m:
            r=mid
        else:
            l=mid+1
    print(int(l+m))
    #print(int(math.ceil((-3+pow(9+4*(2*n-2*m-2),0.5))/2)+1+m))