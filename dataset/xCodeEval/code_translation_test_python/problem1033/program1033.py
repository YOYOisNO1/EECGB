def program1033():
    n,m=map(int,input().split())
    fr=m-1
    sr=n-m
    ans=0
    if(fr<sr):
        ans=m+1
    else:
        ans=m-1
    if(n==1):
        ans=1
    print(ans)