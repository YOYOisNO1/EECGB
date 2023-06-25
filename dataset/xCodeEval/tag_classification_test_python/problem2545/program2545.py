def program2545():
    n=int(input(""))
    k=int(input(""))
    A=int(input(""))
    B=int(input(""))
    
    x=n
    cost=0
    while x>1:
        if x%k==0 and k!=1:
            r=x/k
            s=x-r
            x=r
            if (A*s<B):
                cost=cost+int((A*s))
            else:
                cost=cost+B
        elif k!=1:
            r=int(x%k)
            if x==r:
                x=x-(r-1)
                cost=cost+(r-1)*A
            else:
                x=x-r
                cost=cost+r*A
        else:
            cost=cost+(x-1)*A
            x=1
    
    print(cost)