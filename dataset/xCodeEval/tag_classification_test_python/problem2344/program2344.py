def program2344():
    n=int(input())
    a=list(map(int,input().split()))
    ans=10**10
    for l in range(n):
        for r in range(l,n):
            k1=sum(a[l:r])
            k2=360-k1;
            ans=min(ans,abs(k1-k2))
    print(ans)