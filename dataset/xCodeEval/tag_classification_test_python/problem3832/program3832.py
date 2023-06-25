def program3832():
    a,b,c,n=map(int,input().split())
    if c <= min(a,b) and max(a,b) < n and n-a-b+c >=1:
        print(n-a-b+c)
    else:
        print(-1)