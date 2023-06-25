def program607():
    n,k=map(int,input().split())
    l=[i*5 for i in range(1,n+1)];x=0;i=0
    for i in range(len(l)):
        x=k+sum(l)
        if x<=240:
            print(n)
            break
        else:
            l.pop(-1)
            n-=1
    if k>235:
        print(0)