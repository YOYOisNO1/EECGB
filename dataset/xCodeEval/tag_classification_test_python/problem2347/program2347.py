def program2347():
    I=lambda:map(int,input().split())
    n,=I()
    for i in range(1,5):
        e=I()
        a,b=min(e[:2]),min(e[2:])
        if a+b<=n:
            print(i,a,n-a)
            exit()
    print(-1)