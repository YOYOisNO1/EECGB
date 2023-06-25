def program3152():
    n,k = list(map(int,input().split()))
    p,q,r = ((n*(n-1))//2),((n*(n-1)*(n-2))//6),((n*(n-1)*(n-2)*(n-3))//24)
    if k<2:
        print(1)
    elif k==2:
        print(1+p)
    elif k==3:
        print(1+p+2*q)
    elif k==4:
        print(1+p+2*q+9*r)