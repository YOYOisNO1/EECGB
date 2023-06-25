def program4179():
    n=int(input())
    dp=[1]*(10**6+5)
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            dp[j]+=1
    x=1
    ans=1
    m=998244353
    for i in range(1,n):
        ans=(dp[i+1]+x)%m
        x+=(dp[i+1]+x)%m
    print(ans)
        