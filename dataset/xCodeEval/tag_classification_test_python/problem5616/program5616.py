def program5616():
    from math import *
    m,n=map(int,input().split())
    if m>n:
        t=n;n=m;m=t
    if m==1:
        print(n)
    elif m==2:
        print((n/4)*4+min((n%4),2)*2) 
    else:
        print(int(ceil(n/2.0)*ceil(m/2.0)+(n/2)*(m/2)))
    