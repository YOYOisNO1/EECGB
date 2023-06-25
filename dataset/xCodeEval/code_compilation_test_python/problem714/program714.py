def program714():
    import bisect
    n,m,k=list(map(int,input().split()))
    l=[0]+list(map(int,input().split()))
    l.sort()
    z=k
    x=m
    c=0
    while m>k and k>0: 
        i=bisect.bisect(l,m)
        m=m-l[i-1]
        k=k-1
        c=c+1
    
    if k==0 and m>0:
        c=0
        while z>0:
            z=z-1
            while x>z and i>1:
                i=bisect.bisect(l,x)
                x=x-l[i-1]+1
                c=c+1
        if z==0 and x>0:
            print(-1)
        else:
            print(c)
        
    else:
        print(c)