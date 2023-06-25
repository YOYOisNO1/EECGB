def program510():
    import math as mm
    n,m=map(int,input().split())
    if m==0:
        print(1)
    else:
    
        if n%2==0:
            if m<=n//2:
                print(m)
            else:
                print(n-m)
        else:
            if m<=mm.floor(n/2):
                print(m)
            elif m==mm.floor(n/2)+1:
                print(m-1)
            else:
                print(n-m)