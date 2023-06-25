    mod=int(1e9+7)
    n,k,d=map(int,input().split())
    dp=[[-1 for _ in ' '*2] for _ in range(101) ]
def ktree(sum,ch):
        if sum>n:
            return 0
        if sum==n:
            if ch:
                return 1
            else:return 0
        if dp[sum][ch]!=-1:
            return dp[sum][ch]
        ans=0
        for i in range(1,k+1):
            if i<d:
                ans+=ktree(sum+i,ch)%mod
            else:ans+=ktree(sum+i,1)
        dp[sum][ch]=ans%mod
        return ans%mod
    print(ktree(0,0))