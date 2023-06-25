def program3423():
    n,m=map(int,input().split())
    if not(n==1 and m==1) and m>n:
        print(-1)
    else:
        for i in range(m,n+1,m):
            if i*2>=n:
                print(i)
                break