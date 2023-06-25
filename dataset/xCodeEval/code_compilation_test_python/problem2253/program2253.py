def program2253():
    a=[1]
    n,m=map(int,input().split())
    for i in range(1,n+1):
    	a.append(a[-1]*i)
    ans=0
    for i in range(1,n+1):
    	p=a[i]*a[n-i+1]*(n-i+1)
    	ans+=p
    	ans%=m
    print(ans)