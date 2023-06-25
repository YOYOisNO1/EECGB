def program7337():
    import math
    from decimal import *
    getcontext().prec = 30
    n,m=map(int,input().split())
    ans=0
    if n<m:
        n,m=m,n
    if n<3 and m<3:
        ans=0
    elif m==1:
        ans+=(n//6)*6
        n%=6
        if n>3:
            ans+=(n-3)*2
    elif n%4==0 or m%4==0 or n%6==0 or m%6==0:
        ans=n*m
    elif n<=5 and m<=5:
        if n%2 and m%2:
            ans=n*m-1
        elif n==3:
            ans=n*m-2
        else :
            ans=n*m
    elif n*m==14:
        ans=12
    else :
        ans=n*m//2*2
    print(ans)
    