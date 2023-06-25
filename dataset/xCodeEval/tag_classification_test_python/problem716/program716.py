def program716():
    n,l,r=map(int,input().split())
    if n<2:
        print(1,1)
    elif l<2 and r<2:
        print(n,n)
    else:
        lmin=0
        lmax=0
        for i in range(1,l):
            lmin+=2**i
        lmin+=(n-l+1)
        for i in range(1,r):
            lmax+=2**i
        lmax+=1
        lmax+=(n-r)*2**i
        print(lmin,lmax)