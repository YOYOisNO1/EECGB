def program2363():
    n,m,a,b=map(int,input().split())
    if n%m:
        more=m-n%m
        less=n%m
        print(min(more*a,less*b))
    else: print(0)