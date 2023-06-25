    t=int(input())
    pow2=[1 for x in range(2*100000+1)]
    mod=10**9+7
    for i in range(1,200000+1):
        pow2[i]=pow2[i-1]*2
        pow2[i]%=mod
def solve(k,n):
        if k==0:
            return 1
        if dp[k]!=-1:
            return dp[k]
    
        if n%2==0:
            ans=pow22[k-1]-solve(k-1,n)
            ans+=solve(k-1,n)*pow2[n-1]
            ans%=mod
        else:
            ans=solve(k-1,n)
            ans+=solve(k-1,n)*pow2[n-1]
            ans%=mod
        dp[k]=ans
        return ans
    
    while t:
        t-=1
        n,k=[int(x) for x in input().split()]
        pow22=[1 for x in range(k+1)]
        for i in range(1,k+1):
            pow22[i]=pow22[i-1]*pow2[n]
            pow22[i]%=mod
        if k==0:
            print(1)
            continue
        dp=[-1 for x in range(k+1)]
        for i in range(1,k):
            solve(i,n)
        print(solve(k,n))