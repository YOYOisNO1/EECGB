def program4509():
    a=[]
    n,m=map(int,input().split())
    ans=0
    s=1
    for i in range(0,250001):
        if i>0:
            s=s*i%m
        a.append(s)
    for i in range(1,n+1):
        ans=(ans+(n-i+1)*a[n-i+1]*a[i])%m
    print(ans%m)