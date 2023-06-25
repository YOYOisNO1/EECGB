def program2644():
    import math
    n,m,a,b=map(int,input().split())
    if b/m>=a:
        print(int(n*a))
    else:
        if n%m==0:
            print(int((n/m)*b))
        else:
            mt=int((n/m))*b
            ot=(n%m)*a
            tmt=math.ceil(n/m)*b
            mn=min(ot+mt,tmt)
            # print(tmt,ot)
            print(int(mn))