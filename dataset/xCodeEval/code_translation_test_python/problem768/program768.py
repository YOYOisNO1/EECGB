def program768():
    n,k = map(int,input().split())
    x = ((n-1)*2) + 3
    if k==1 or k==n:
        x+=(n-1)
    else:
        if k-1<=n-k:
            x+=(k-1)*2
            x+=n-k
        else:
            x+=(n-k)*2
            x+=(k-1)
    print(x)