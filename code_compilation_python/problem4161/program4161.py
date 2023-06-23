def program4161():
    n,m,s=list(map(int,input().split()))
    if (s+1)**2==n*m:
        print(4)
    else:
        print(n*m)