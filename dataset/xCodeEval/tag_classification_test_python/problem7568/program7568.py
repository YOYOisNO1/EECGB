def program7568():
    import sys
    
    n,m,k=map(int,input().split())
    d = 1 if input()=='to tail' else -1
    for i,c in enumerate(input()):
        if c=='0':
            if m<k and m>1: m-=1
            elif m>k and m<n: m+=1
            k+=d
            if k<1 or k>n:
                k-=2*d
                d=-d
            if m==k:
                print("Controller"), i+1
                sys.exit(0)
        else:
            m+=d
            k+=d
            if k<1 or k>n:
                k-=2*d
                d=-d
            if 1<=k-d<=n: m=k-d
            else: m=k+d
    print("Stowaway")