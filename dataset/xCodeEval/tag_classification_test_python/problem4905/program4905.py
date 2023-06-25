def program4905():
    x=int(input())
    prim=[0]*(x+1)
    for n in range(2,x+1):
        if not prim[n]:
            #prim[n]=n
            for k in range(2*n,x+1,n):
                prim[k]=n
    
    p=prim[x]
    res=1e9
    for n in range(x-p+1,x+1):
        cur=n
        mxp=prim[cur]
        d=cur-mxp+1
        res=min(res,d)
    
    print(res)
    