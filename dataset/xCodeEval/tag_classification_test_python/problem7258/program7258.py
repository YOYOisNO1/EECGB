def program7258():
    from decimal import *
    import sys
    getcontext().prec=100
    n,m=input().split()
    n=eval(n)
    m=eval(m)
    if n*m<=2:
        if n==2 and m==1:
            print(0.5)
        else:
            print(1)
        sys.exit()
    n=Decimal(n)
    m=Decimal(m)
    a=m*n
    b=n-1
    b=b*b
    ans=(a-1+(n-1)*(m-1))/(n*(a-1))
    print(ans)